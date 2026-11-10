---
name: video-prompt-rea
description: Reverse engineer prompts, cinematographic style, camera trajectory, and generation pipelines from any video URL (Twitter/X, YouTube, TikTok, direct MP4) or local video file using REA (Reverse Engineering Analysis). Reconstructs exact, production-ready prompts for Runway Gen-3, Kling AI, Luma Dream Machine, Sora, Hailuo/Minimax, Midjourney I2V, or Motion Graphics specs.
---

# Video Prompt REA (Reverse Engineering Analysis)

Reverse engineer any video into its foundational creative and technical ingredients: prompt structure, cinematographic language, lighting, physics, and model-specific syntax.

---

## 1. When to Use This Skill

Activate this skill when the user:
- Provides a video link (e.g. X/Twitter, YouTube, Instagram, TikTok, direct MP4 link) or a local video path.
- Asks: *"How was this video generated?"*, *"What was the prompt for this video?"*, or *"Do a REA on this video"*.
- Wants to replicate the visual style, camera motion, or aesthetic of an existing video in Runway, Kling, Luma, Sora, or Midjourney.

---

## 2. Ingestion & Preprocessing

When a video source (URL or file) is provided:

1. **Extract frames and metadata**:
   Run the bundled extraction script:
   ```bash
   python3 ~/.agents/skills/video-prompt-rea/scripts/extract_frames.py "<VIDEO_URL_OR_PATH>" --num-frames 6 --output-dir /tmp/rea_video
   ```
2. **Inspect the extracted frames**:
   Read the generated frames in `/tmp/rea_video/frames/` using visual inspection tools to analyze key moments, transitions, and camera movement over time.
   *(Note: If running in Claude Projects or ChatGPT where terminal execution is not available, ask the user to upload the video or 3-5 screenshots from start, middle, and end).*

---

## 3. The 4-Layer REA Decomposition Framework

Analyze the video across four distinct analytical layers:

### Layer 1: Pipeline & Archetype Identification
Determine which production pipeline created the video:
- **Archetype A: Pure AI Video (Text-to-Video / T2V)**: Generated straight from text (e.g. Sora, Runway Gen-3, Kling, Hailuo). Signs: fluid morphing, AI temporal diffusion textures, complex micro-motion.
- **Archetype B: Image-to-Video (I2V)**: A high-fidelity static image (Midjourney v6, Flux.1) animated via video diffusion (Kling, Runway, Luma). Signs: hyper-crisp first frame with motion added subsequently.
- **Archetype C: 3D / Motion Graphics / Hybrid Launch Video**: High-end product launch (e.g. @shapelayer / LaunchAnything style). Signs: vector UI, isometric 3D mockups, precise geometric easing curves, typography.
- **Archetype D: Stylized / VFX Composite**: Live action or CGI with AI style transfer or particle overlay.

### Layer 2: Visual Composition & Subject Anatomy
- **Subject**: Primary subject, character appearance, materials (glass, matte metal, cloth, skin), posture.
- **Environment & Backdrop**: Studio void, architectural setting, interior, natural landscape, atmospheric haze.
- **Lighting & Color**:
  - Key, fill, and rim light positioning.
  - Quality: diffuse softbox, hard direct sunlight, neon glow, specular highlights.
  - Color palette: primary, secondary, and accent hex/tone families; LUT style (e.g. Kodak 5207, Apple clean high-key, cyberpunk dark mode).

### Layer 3: Cinematography & Camera Optics
- **Lens & Framing**: Extreme close-up (ECU), Macro, Medium shot, Establishing wide shot.
- **Focal Length & Depth**: Wide-angle (24mm, slight distortion), Normal (50mm), Portrait telephoto (85mm-100mm with shallow depth of field and soft bokeh).
- **Camera Trajectory**:
  - Linear: Dolly in/out, Truck left/right, Pedestal up/down.
  - Angular: Pan left/right, Tilt up/down, Roll/Dutch angle.
  - Dynamic: Orbital arc, FPV drone dive, handheld micro-jitter, crane shot.
- **Speed & Pacing**: Real-time 24fps cinema, slow-motion (60-120fps), hyperlapse, dynamic speed ramp.

### Layer 4: Temporal Dynamics & Physics
- Fluid dynamics, smoke/particles, gravity, cloth simulation, UI card animations, transitions (match-cut, whip-pan, morph).

---

## 4. Output Specification

Present the REA report in a clean, structured format with ready-to-copy prompts:

```markdown
# 🎬 REA Video Deconstruction: [Video Title / Concept]

## 1. Pipeline Classification
- **Primary Archetype**: [T2V | I2V | 3D Motion Graphics Hybrid]
- **Target Resolution & Aspect Ratio**: [e.g. 3840x2160, 16:9]
- **Estimated Source Tools**: [e.g. Midjourney v6 + Kling 1.5 | Runway Gen-3 Alpha | After Effects + 3D Render]

## 2. Core Visual Ingredients
- **Subject**: [Detailed breakdown]
- **Lighting & Palette**: [Lighting setup, color tones]
- **Cinematography & Camera**: [Focal length, movement vector, speed]

---

## 3. Reconstructed AI Prompts

### 🔹 Universal Master Prompt
> [Detailed prose capturing the entire visual narrative, style, lighting, and camera motion in 2-3 sentences]

### 🔹 Runway Gen-3 Alpha
```text
[Camera movement syntax]: [Subject description] [action/motion dynamics]. [Lighting and environment]. [Cinematic lens & aesthetic tags].
```

### 🔹 Kling AI (v1.5)
```text
[Subject and action], [scenery details], [lighting]. Camera: [Pan/Tilt/Zoom instructions].
--camera-zoom [in/out] --camera-pan [left/right] --motion-magnitude [1-10]
```

### 🔹 Luma Dream Machine
```text
[Camera move directive], [subject doing action], [lighting & physical realism details], cinematic 4k, 35mm lens.
```

### 🔹 Midjourney v6 / Flux.1 (If using Image-to-Video workflow)
```text
[Subject, composition, lighting, materials, camera angle] --ar 16:9 --style raw --v 6.1
```

### 🔹 Motion Graphics / Technical Specs (If 3D / Tech Launch Video)
- **Easing**: [e.g. Cubic-bezier(0.25, 1, 0.5, 1) / Smooth Out]
- **3D Assets & Lighting**: [e.g. Space Grey Apple MacBook Pro 16", Softbox 5500K left, Warm 2700K lamp right]
- **Animation Stack**: [e.g. After Effects / Remotion / Three.js / Spline]
```

---

## 5. References & Model Guides
- For model-specific prompt tokens, see `references/model_syntax.md`.
- For cinematographic terminology, see `references/cinematography_glossary.md`.
