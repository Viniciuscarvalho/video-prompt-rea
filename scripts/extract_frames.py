#!/usr/bin/env python3
"""
extract_frames.py - Helper script for video-prompt-rea skill.
Downloads or ingests a video, probes metadata, and extracts keyframes for visual REA analysis.
Zero external pip dependencies (uses built-in urllib, json, subprocess, shutil).
Requires: ffmpeg (found in /opt/homebrew/bin, /usr/local/bin, or PATH).
Optional: yt-dlp for arbitrary video platforms.
"""

import sys
import os
import re
import json
import argparse
import subprocess
import shutil
import urllib.request
from pathlib import Path

def find_binary(name):
    # Check standard locations
    for directory in ["/opt/homebrew/bin", "/usr/local/bin", "/usr/bin", "/bin"]:
        p = os.path.join(directory, name)
        if os.path.isfile(p) and os.access(p, os.X_OK):
            return p
    return shutil.which(name)

def resolve_x_video_url(tweet_url):
    """Resolve Twitter / X status URL to direct MP4 using fxtwitter API."""
    match = re.search(r'(?:twitter\.com|x\.com)/([^/]+)/status/(\d+)', tweet_url)
    if not match:
        return None
    user, status_id = match.groups()
    api_url = f"https://api.fxtwitter.com/{user}/status/{status_id}"
    req = urllib.request.Request(api_url, headers={"User-Agent": "Mozilla/5.0 (Agentic-Video-REA)"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            tweet = data.get("tweet", {})
            media = tweet.get("media", {})
            videos = media.get("videos", []) or [m for m in media.get("all", []) if m.get("type") == "video"]
            if videos:
                formats = videos[0].get("formats", [])
                # Sort by bitrate or resolution descending to get best quality MP4
                mp4_formats = [f for f in formats if f.get("container") == "mp4" or "mp4" in f.get("url", "")]
                if mp4_formats:
                    # Pick highest bitrate or 1080p
                    mp4_formats.sort(key=lambda x: x.get("bitrate", 0), reverse=True)
                    return mp4_formats[0].get("url")
                return videos[0].get("url")
    except Exception as e:
        sys.stderr.write(f"FXTwitter resolution failed: {e}\n")
    return None

def download_file(url, target_path):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Agentic-Video-REA)"})
    with urllib.request.urlopen(req, timeout=60) as resp, open(target_path, "wb") as out_file:
        shutil.copyfileobj(resp, out_file)
    return target_path

def get_video_info(ffprobe_path, video_path):
    cmd = [
        ffprobe_path,
        "-v", "quiet",
        "-print_format", "json",
        "-show_format",
        "-show_streams",
        video_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        return {}
    data = json.loads(res.stdout)
    duration = float(data.get("format", {}).get("duration", 0))
    video_stream = next((s for s in data.get("streams", []) if s.get("codec_type") == "video"), {})
    width = video_stream.get("width")
    height = video_stream.get("height")
    r_frame_rate = video_stream.get("r_frame_rate", "30/1")
    try:
        num, den = map(int, r_frame_rate.split('/'))
        fps = round(num / den, 2) if den != 0 else 30.0
    except Exception:
        fps = 30.0
    
    return {
        "duration": duration,
        "width": width,
        "height": height,
        "fps": fps,
        "codec": video_stream.get("codec_name", "unknown")
    }

def main():
    parser = argparse.ArgumentParser(description="Extract metadata and keyframes from video for REA analysis.")
    parser.add_argument("source", help="URL or local path to the video file")
    parser.add_argument("--num-frames", type=int, default=6, help="Number of frames to extract across duration")
    parser.add_argument("--output-dir", default="./rea_output", help="Directory to save extracted frames")
    args = parser.parse_args()

    ffmpeg_bin = find_binary("ffmpeg")
    ffprobe_bin = find_binary("ffprobe")
    yt_dlp_bin = find_binary("yt-dlp")

    if not ffmpeg_bin:
        sys.stderr.write("Error: ffmpeg is required but not found in PATH or standard directories.\n")
        sys.exit(1)

    out_dir = Path(args.output_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    frames_dir = out_dir / "frames"
    frames_dir.mkdir(parents=True, exist_ok=True)

    video_path = None
    source = args.source.strip()

    # Step 1: Ingest Video
    if os.path.exists(source):
        video_path = str(Path(source).resolve())
    elif source.startswith("http://") or source.startswith("https://"):
        direct_url = None
        if "twitter.com" in source or "x.com" in source:
            direct_url = resolve_x_video_url(source)
            if not direct_url and yt_dlp_bin:
                pass # fallback to yt-dlp below
        
        target_video = out_dir / "input_video.mp4"
        if direct_url:
            sys.stderr.write(f"Resolved direct video stream: {direct_url}\n")
            download_file(direct_url, target_video)
            video_path = str(target_video)
        elif yt_dlp_bin:
            sys.stderr.write(f"Downloading with yt-dlp: {source}\n")
            cmd = [yt_dlp_bin, "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best", "-o", str(target_video), source]
            subprocess.run(cmd, check=True)
            video_path = str(target_video)
        else:
            # Try direct download if ends in video extension
            if any(source.endswith(ext) for ext in [".mp4", ".mov", ".webm", ".mkv"]):
                download_file(source, target_video)
                video_path = str(target_video)
            else:
                sys.stderr.write("Error: Could not resolve video URL. Please install yt-dlp (brew install yt-dlp) or pass a direct MP4 link / local file.\n")
                sys.exit(1)
    else:
        sys.stderr.write(f"Error: Source not found or invalid: {source}\n")
        sys.exit(1)

    # Step 2: Probe Video Metadata
    info = get_video_info(ffprobe_bin, video_path) if ffprobe_bin else {}
    duration = info.get("duration", 5.0)

    # Step 3: Extract Keyframes
    num_frames = max(args.num_frames, 2)
    timestamps = []
    if duration > 0:
        step = duration / (num_frames - 1) if num_frames > 1 else duration
        for i in range(num_frames):
            t = min(i * step, max(0.0, duration - 0.1))
            timestamps.append(t)
    else:
        timestamps = [0.0]

    extracted_frames = []
    for idx, ts in enumerate(timestamps):
        frame_filename = f"frame_{idx:02d}_t{ts:.2f}s.jpg"
        frame_path = frames_dir / frame_filename
        cmd = [
            ffmpeg_bin,
            "-y",
            "-ss", f"{ts:.3f}",
            "-i", video_path,
            "-frames:v", "1",
            "-q:v", "2",
            str(frame_path)
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if frame_path.exists():
            extracted_frames.append({
                "index": idx,
                "timestamp": round(ts, 2),
                "path": str(frame_path)
            })

    output_result = {
        "status": "success",
        "source": source,
        "video_path": video_path,
        "metadata": {
            "duration": round(duration, 2),
            "width": info.get("width"),
            "height": info.get("height"),
            "fps": info.get("fps"),
            "codec": info.get("codec")
        },
        "frames": extracted_frames
    }

    print(json.dumps(output_result, indent=2))

if __name__ == "__main__":
    main()
