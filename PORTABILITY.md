# Portability Guide: Using Video Prompt REA in Other AI Tools

This skill is designed following open Agentic Skill conventions (markdown + YAML frontmatter + modular references + standalone scripts). You can easily take it to any other AI platform:

---

## 1. Using in Claude Code CLI

Claude Code natively supports agent skills placed in `.agents/skills/` or `~/.agents/skills/`.
Since this skill is located at `~/.agents/skills/video-prompt-rea/`, **Claude Code already discovers it automatically**!

To trigger it in Claude Code:
```bash
claude "Do a video REA on https://x.com/shapelayer/status/2119836576750395719"
```

---

## 2. Using in Claude Projects / Claude.ai (Web / Desktop)

1. Open your **Project** in Claude.ai (or open a new chat).
2. In **Project Knowledge**, upload:
   - `SKILL.md`
   - `references/model_syntax.md`
   - `references/cinematography_glossary.md`
3. In **Custom Instructions (System Prompt)**, paste:
   ```text
   You are an expert in Reverse Engineering Analysis (REA) for generative video. When the user provides a video description, frames, or link, activate the video-prompt-rea skill from your knowledge base to deconstruct the visual pipeline and output exact, production-ready prompts for Runway Gen-3, Kling AI, Luma Dream Machine, Sora, and Midjourney.
   ```
4. **How to use in chat**:
   Upload the video file or 3-5 screenshots from the video and ask: *"Fazer REA deste vídeo para extrair o prompt"*.

---

## 3. Using in OpenAI Codex / ChatGPT Custom GPT

1. Go to **ChatGPT > Explore GPTs > Create a GPT**.
2. Under **Configure**:
   - **Name**: Video Prompt REA Engineer
   - **Description**: Reverse engineer generative video prompts and cinematographic pipelines.
   - **Instructions**: Copy the entire text from `SKILL.md`.
   - **Knowledge**: Upload `model_syntax.md` and `cinematography_glossary.md`.
   - **Capabilities**: Enable *Code Interpreter* (Advanced Data Analysis) and *Web Browsing*.
3. With Code Interpreter enabled, ChatGPT can even run python code or accept video uploads directly!

---

## 4. Standalone Terminal Use

You can run the extraction script anywhere from your terminal:
```bash
python3 ~/.agents/skills/video-prompt-rea/scripts/extract_frames.py "https://x.com/user/status/123456" --num-frames 6
```
This downloads the video and extracts frames into `./rea_output/frames/`.
