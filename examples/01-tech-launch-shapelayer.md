# Case Study 01: Tech Launch Video REA (@shapelayer / Ren AI)

## Input
- **Source**: `https://x.com/shapelayer/status/2119836576750395719`
- **Creator**: Leon Fucak (@shapelayer - LaunchAnything)
- **Tagline**: *"Launch videos never looked this clean"*

---

## 1. Pipeline Classification
- **Primary Archetype**: Hybrid 3D Motion Graphics + UI Compositing (Apple / Linear / LaunchAnything design vernacular).
- **Target Resolution**: 3840x2160 (4K UHD) @ 30fps.
- **Estimated Source Tools**: Cinema4D / Blender (Octane or Redshift render engine) + Figma / After Effects + Remotion.

---

## 2. Visual & Cinematographic Ingredients
- **Lighting**: Split color temperature — warm 2700K incandescent desk lamp on camera right, contrasting with cool 6500K twilight ambient exterior light through the window on camera left.
- **Camera Dynamics**: Subtle slow push-in (dolly forward) with custom cubic bezier easing; optical rack focus blurring the background cards to direct viewer eye tracking.
- **Aesthetic Tone**: Ultra-clean high-key studio white; soft ambient contact shadows; subtle glassmorphism and glossy chrome reflections.

---

## 3. Reconstructed Prompts

### Image Base (Midjourney v6.1 / Flux.1) — Hero Frame
```text
A cinematic ultra-clean close-up shot of a modern dark space-grey 16-inch laptop open on a warm rustic wooden desk, crisp illuminated display showing a minimalist modern web interface, warm glowing desk lamp casting soft golden light on the right, cool blue twilight window light from the left, shallow depth of field, sharp screen details, shot on 35mm lens, f/2.0 aperture, Apple commercial aesthetic --ar 16:9 --style raw --v 6.1
```

### Runway Gen-3 Alpha — Hardware Push-In
```text
Slow smooth cinematic push-in: High-end space-grey laptop open on a textured oak desk, displaying a glowing white software interface. Soft warm practical lamp light highlights the edge of the keyboard, subtle dust particles floating in air, shallow depth of field, high dynamic range, 4k commercial grade, photorealistic.
```

### Runway Gen-3 Alpha — 3D Character Mascot & Floating Cards
```text
Micro orbital pan around subject: A sleek iridescent metallic floating sphere character with subtle happy facial dots hovering above clean white glassmorphic interface cards. Soft diffuse studio lighting, subtle pink and chrome reflections, smooth physics easing, pristine minimalist aesthetic.
```

### Kling AI (v1.5)
```text
Close-up product commercial of a modern sleek space-grey laptop on a wooden desk, screen glowing with clean software dashboard, warm ambient desk lamp light, slow cinematic camera zoom in.
--camera-zoom in --motion-magnitude 3
```

### Motion Graphics & Frontend Code Specs
- **Animation Easing**: `cubic-bezier(0.16, 1, 0.3, 1)` (Fluid spring deceleration).
- **Typography**: San Francisco Pro Display / Inter.
- **Shadow Stack**: `box-shadow: 0 20px 40px -15px rgba(0,0,0,0.06), 0 0 1px rgba(0,0,0,0.1)`.
