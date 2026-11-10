#!/usr/bin/env bash
# install.sh - Universal installer for video-prompt-rea skill
# Links the skill into ~/.agents/skills and AI agent environments (Antigravity, Claude Code, etc.)

set -e

SKILL_NAME="video-prompt-rea"
SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🚀 Installing ${SKILL_NAME} from: ${SOURCE_DIR}"

# 1. Target directories
AGENTS_SKILLS_DIR="${HOME}/.agents/skills"
GEMINI_ANTIGRAVITY_DIR="${HOME}/.gemini/antigravity/skills"
GEMINI_SKILLS_DIR="${HOME}/.gemini/skills"

mkdir -p "${AGENTS_SKILLS_DIR}"

# 2. Link into ~/.agents/skills (Standard Agent Skills location used by Claude Code)
TARGET_LINK="${AGENTS_SKILLS_DIR}/${SKILL_NAME}"
if [ -L "${TARGET_LINK}" ] || [ -d "${TARGET_LINK}" ]; then
    rm -rf "${TARGET_LINK}"
fi
ln -sf "${SOURCE_DIR}" "${TARGET_LINK}"
echo "  ✓ Linked to ${TARGET_LINK} (Claude Code & Agents standard)"

# 3. Link into Antigravity / Gemini if directories exist
if [ -d "${HOME}/.gemini" ]; then
    mkdir -p "${GEMINI_ANTIGRAVITY_DIR}" "${GEMINI_SKILLS_DIR}"
    ln -sf "${TARGET_LINK}" "${GEMINI_ANTIGRAVITY_DIR}/${SKILL_NAME}"
    ln -sf "${TARGET_LINK}" "${GEMINI_SKILLS_DIR}/${SKILL_NAME}"
    echo "  ✓ Linked to Antigravity (${GEMINI_ANTIGRAVITY_DIR}/${SKILL_NAME})"
fi

# 4. Check dependencies
echo ""
echo "🔍 Checking system dependencies..."

if command -v ffmpeg >/dev/null 2>&1 || [ -x "/opt/homebrew/bin/ffmpeg" ]; then
    echo "  ✓ ffmpeg is available"
else
    echo "  ⚠️  ffmpeg not detected in PATH. Highly recommended for keyframe extraction:"
    echo "      macOS: brew install ffmpeg"
    echo "      Ubuntu/Debian: sudo apt update && sudo apt install -y ffmpeg"
fi

if command -v yt-dlp >/dev/null 2>&1 || [ -x "/opt/homebrew/bin/yt-dlp" ]; then
    echo "  ✓ yt-dlp is available (supports YouTube, TikTok, Instagram, etc.)"
else
    echo "  ℹ️  yt-dlp is optional (Twitter/X uses built-in API, but yt-dlp is recommended for other platforms):"
    echo "      macOS: brew install yt-dlp"
fi

echo ""
echo "🎉 Installation complete!"
echo ""
echo "To use this skill:"
echo "  • In Antigravity or Claude Code: Ask 'Do a video REA on <URL>' or 'Extraia o prompt do vídeo <URL>'"
echo "  • CLI extraction test: python3 ${SOURCE_DIR}/scripts/extract_frames.py '<VIDEO_URL>'"
echo "  • Portability guide: see ${SOURCE_DIR}/PORTABILITY.md"
