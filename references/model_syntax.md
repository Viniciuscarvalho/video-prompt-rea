# AI Video Models Syntax & Prompting Cheat Sheet

This reference document outlines the syntax conventions, parameter tags, and best practices for prompting the major generative video platforms.

---

## 1. Runway Gen-3 Alpha

Runway Gen-3 works best with **structured, camera-first descriptive prompts**. It interprets directional commands and cinematic lighting with high fidelity.

### Recommended Structure:
```text
[Camera movement]: [Subject] [Detailed action / movement]. [Environment and background elements]. [Lighting style and color temperature]. [Cinematic optics and film stock].
```

### Syntax Examples:
- **Low Angle Tracking Shot**:
  `Low-angle tracking shot pushing forward: A sleek cybernetic athlete sprinting through a mist-filled neon Tokyo alleyway. Neon signs reflect off wet asphalt puddles. Diffused blue and magenta rim lighting, cinematic 35mm lens, anamorphic lens flare, photorealistic 8k.`
- **FPV / Dynamic Fly-through**:
  `Fast continuous FPV drone dive: swooping through the interior of a sunlit modern brutalist concrete villa, gliding over an infinity pool toward the ocean horizon at sunset. Warm golden hour light, motion blur on edges, hyper-smooth gimbal stabilization.`

### Key Runway Camera Keywords:
- Movements: `Slow dolly in`, `Dolly zoom (vertigo effect)`, `Continuous orbital camera around subject`, `Static camera with subject motion`, `Overhead top-down bird's eye view`, `Smooth pan left to right`.

---

## 2. Kling AI (v1.0 & v1.5)

Kling AI excels at **human anatomy, physical interaction, and high-fidelity motion**. It accepts both natural language instructions and dedicated camera control UI parameters.

### Recommended Structure:
```text
[Subject with precise descriptive attributes], [dynamic action or physical interaction], [setting/background], [lighting and atmosphere], [camera angle and motion direction].
```

### Motion & Camera Controls in Kling:
- **Motion Magnitude**: Controls the intensity of motion (`1` = subtle breathing/ambient, `10` = fast dynamic action).
- **Camera Movement Types**:
  - Horizontal: `Pan Left`, `Pan Right`
  - Vertical: `Tilt Up`, `Tilt Down`
  - Depth: `Zoom In`, `Zoom Out`
  - Roll: `Clockwise Roll`, `Counter-Clockwise Roll`
- **Prompt Formula for Kling**:
  `Close-up cinematic shot of an astronaut adjusting the helmet visor inside an illuminated spaceship cockpit. Reflections of Earth visible in the glass. The camera slowly zooms in as the astronaut breathes gently. Soft volumetric blue interior lighting, 8k resolution, cinematic color grading.`

---

## 3. Luma Dream Machine

Luma Dream Machine is built on high-fidelity physical world simulation and camera movement awareness.

### Prompting Principles:
- Use direct natural camera instructions: `camera pans right to reveal...`, `push in smoothly...`, `crane shot descending down...`.
- Describe physics and weight: fluid pouring, cloth billowing in wind, dust dancing in sunbeams.
- Avoid keyword spamming (e.g. "photorealistic, 8k, trending on artstation"); use descriptive lighting and optics instead.

### Example:
```text
Smooth cinematic push in on a vintage espresso machine brewing coffee into a ceramic cup in a quiet Parisian cafe on a rainy morning. Rich crema forms as warm amber light hits the steam rising. Shallow depth of field, 50mm f/1.8 lens.
```

---

## 4. Sora & Hailuo AI (Minimax)

Both Sora and Hailuo AI (Minimax) possess deep spatial and temporal comprehension. They interpret dense, literary cinematic descriptions with extreme narrative coherence.

### Prompting Principles:
- Describe temporal sequence: *"First X happens, then the camera transitions to reveal Y..."*
- Detail spatial relationships: foreground, midground, background interactions.
- Specify lens properties and sensor behavior: *"captured on 70mm IMAX film, natural color science, fine cinematic grain"*.

---

## 5. Image-to-Video (I2V) Pipeline: Midjourney / Flux + Motion

For maximum aesthetic control, professional creators often use a two-step pipeline:
1. **Hero Frame Generation (Midjourney v6.1 or Flux.1)**:
   - Midjourney syntax: `[Subject, scene, composition, lens, lighting] --ar 16:9 --style raw --v 6.1`
   - Flux.1 syntax: Natural language prompt focusing on realism and texture detail.
2. **Video Animation (Runway / Kling / Luma)**:
   - Provide the initial image as start frame.
   - Text prompt only needs to describe **the delta (what moves)**:
     - `The character looks up and smiles softly as the wind gently moves their hair. Soft camera dolly in.`
     - Avoid re-describing the static objects already present in the image.
