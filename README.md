# Kamelion

Kamelion is a high-fidelity standalone desktop software application engineered for PC and Mac that bridges the gap between 2D digital imagery and multi-material physical 3D prints. By incorporating advanced, real-time image analysis alongside direct hardware calibration loops, Kamelion lets you design and control complex translucent filament layering without the guesswork.

## 🦎 Core Interface Philosophy

Kamelion is designed with an on-demand, clutter-free user interface context. Instead of overwhelming your workspace with persistent control blocks, a clean desktop header handles global parameters, leaving the workspace completely dedicated to your active creative canvas.

*   **Adaptive Dual-Window System:** The layout boots into a split framework featuring a *Preview Window* on the left for direct drag-and-drop or click-to-load asset ingestion, alongside a *Studio Window* on the right displaying a fixed monochrome depth simulation. Upon executing background calculations, the initial preview container collapses automatically, expanding the Studio Window full-screen into your primary layout viewport.
*   **On-Demand Toolsets Panel:** Granular adjustments—such as region masking brushes or manual sliding thickness bars—are contained within hidden, expandable panels that slide into view only when explicitly triggered by the user, keeping the main interface completely streamlined.

## 🛠️ Integrated Feature Modules

The software framework is driven by a series of specialized underlying code sub-routines:

### 1. `Filter_CLAHE` (Shadow Detail Boost)
An automated background contrast-limiting adaptive histogram equalization matrix that activates immediately upon asset loading. It optimizes local features and eliminates dark crushed shadow gradients, exposing hidden variations in your source graphic to produce smoother physical layer gradients. An optional on/off toggle button sits right beneath your active viewport for on-the-fly comparisons.

### 2. `Mode_FrontLit` & `Mode_BackLit` (Slicing Profiles)
*   **Mode_FrontLit (Surface Painting):** Calibrates the mathematical slicing engine to build opaque reflective layering optimized for front-facing ambient light.
*   **Mode_BackLit (Lithophane):** Shifts the depth matrix to optimize light transmission and translucent bleeding effects, utilizing back-lighting sources to resolve the image details.

### 3. `Function_SpotInjection` (Color Pop Masking)
A coordinate-tracking paint utility that allows users to isolate precise regions (e.g., lips, eyes, or foreground highlights) directly on top of the grayscale simulation canvas. Tracing a feature automatically opens a focused, on-demand color inventory popup palette. Once a filament color is assigned, the software injects localized color-swapping instructions at those exact coordinate heights while leaving the surrounding background grayscale layers un-altered.

### 4. `Hardware_TD1_Listener` (Fail-Safe Connectivity)
A dedicated background daemon channel that communicates with connected TD-1/TD1S optical transmission distance sensors via a standard Virtual COM Port over USB or Bluetooth serial pathways. 
*   **Automated Pop-In Handshake:** When a physical tool connection is detected, a temporary notification card registers the event and automatically slides the calibration menu into the center of the workspace screen.
*   **Manual Initialization Fail-Safe:** If an operating system level port glitch blocks auto-discovery routines, a manual `Initialize TD-1 Tool` override option inside the `File` menu forces a low-level DTR/RTS serial line reset to wake up the sensor chip and re-establish a data stream instantly.
*   **Color Swatch Spectrum Correction:** If an optical reading misinterprets a highly saturated translucent filament (e.g., mistaking a deep midnight navy blue for pure black), clicking the integrated color swatch pops open an expanding left-to-right gradient palette, allowing the user to override the color manually before committing changes.

## 📁 Repository Directory Map

Structure your repository directories inside your online GitHub interface following this clean layout framework to match the compiler paths:

```text
kamelion/
│
├── .gitignore               # System exclusions cache tracking block
├── requirements.txt         # Dependent third-party Python module registry
├── installer_setup.py       # Standalone executable packaging engine utility
│
├── data/
│   └── kamelion_filaments.json  # Local filament library inventory document
│
└── src/
    ├── app_main.py          # Main application loop entry point
    ├── gui_workspace.py     # Custom silver and sea-green interface screens
    ├── hardware_listener.py # Background serial COM port monitoring daemon
    └── database_manager.py  # Structured library file synchronization script
```

## 🚀 Setup & Execution Guide

### Local Package Installation
To install the dependent processing engines listed in your `requirements.txt` file, run the following command in your terminal window:
```bash
pip install -r requirements.txt
```

### Distributing Desktop Builds
Once your Python script blocks are fully finalized inside your `src/` directory, you can build a completely independent, shareable desktop application package by executing the installer script:
```bash
python installer_setup.py
```
This utility compiles your modules into a standalone package directory located inside `/dist/Kamelion/`. You can copy or compress this folder and pass it directly to friends or makers, allowing them to run the software offline on their computers out of the box.
