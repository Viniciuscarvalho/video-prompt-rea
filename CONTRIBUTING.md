# Contributing to video-prompt-rea

Thank you for your interest in contributing to **video-prompt-rea**! We welcome contributions from prompt engineers, AI filmmakers, motion designers, and developers.

---

## 🛠 Ways to Contribute

1. **Add Support for New Video Models**:
   - As new video foundation models launch (e.g. Wan2.1, HunyuanVideo, CogVideoX, Hailuo update, Sora updates), add their syntax, camera tokens, and prompting conventions to [`references/model_syntax.md`](references/model_syntax.md).
2. **Expand Cinematography Terms**:
   - Add new camera movements, lighting terms, or lens characteristics to [`references/cinematography_glossary.md`](references/cinematography_glossary.md).
3. **Submit Real-World REA Case Studies**:
   - Reverse-engineer impressive videos and add them to the [`examples/`](examples/) directory following the format of existing case studies.
4. **Improve the Extractor Script**:
   - Enhance [`scripts/extract_frames.py`](scripts/extract_frames.py) with better platform resolvers, scene-cut detection, or metadata probing while keeping zero required pip dependencies.

---

## 🚀 Development Workflow

1. **Fork the repository** on GitHub.
2. **Clone your fork**:
   ```bash
   git clone https://github.com/<your-username>/video-prompt-rea.git
   cd video-prompt-rea
   ```
3. **Create a feature branch**:
   ```bash
   git checkout -b feature/model-wan21-syntax
   ```
4. **Make your changes** and test locally:
   - If modifying `extract_frames.py`, test with a sample URL or local file:
     ```bash
     python3 scripts/extract_frames.py "https://x.com/..." --output-dir /tmp/test
     ```
   - Ensure the script runs without errors using Python standard libraries.
5. **Commit your changes**:
   ```bash
   git commit -m "feat(references): add Wan2.1 video model prompting conventions"
   ```
6. **Push to your fork**:
   ```bash
   git push origin feature/model-wan21-syntax
   ```
7. **Open a Pull Request** against `main` on `Viniciuscarvalho/video-prompt-rea`.

---

## 📋 Guidelines

- **Keep Scripts Dependency-Free**: The core extractor script should continue running out-of-the-box on clean Python 3 installations without requiring `pip install`.
- **Accurate Model Syntaxes**: Only add prompt parameters and syntax that have been tested and verified to improve generation quality on that specific model.
- **Clear Markdown**: Use standard GitHub Flavored Markdown for all references and documentation.
