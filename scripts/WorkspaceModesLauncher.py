# Workspace Modes Launcher (Starter Pack)
# Jordan, this script activates different "modes" of your workspace on Windows using AutoHotkey, PowerShell, and FancyZones.
# Each mode launches a set of apps, organizes windows, opens folders or websites, and can trigger additional scripts.

import os
import subprocess
import time
import webbrowser

# Define your modes here
MODES = {
    "3d": {
        "apps": [
            r"C:\Program Files\Blender Foundation\Blender 4.2\blender-launcher.exe",
            r"C:\Users\Jordan\AppData\Local\Autodesk\webdeploy\production\6a0c9611291d45bb9226980209917c3d\FusionLauncher.exe",
            r"C:\Program Files\OrcaSlicer\orca-slicer.exe"
        ],
        "folders": [
            r"C:\Users\Jordan\Documents\3D Printing\models"
        ],
        "web": [
            "https://www.printables.com/",
            "https://makerworld.com/"
        ]
    },
    "design": {
        "apps": [
            r"C:\Program Files\Adobe\Adobe Illustrator 2024\Support Files\Contents\Windows\Illustrator.exe",
            r"C:\Program Files\Adobe\Adobe Photoshop 2024\Photoshop.exe"
        ],
        "folders": [
            r"C:\Users\Jordan\Design\Assets"
        ],
        "web": [
            "https://fonts.google.com/",
            "https://coolors.co/"
        ]
    },
    "content": {
        "apps": [
            r"C:\Program Files\Adobe\Adobe After Effects 2024\Support Files\AfterFX.exe",
            r"C:\Program Files\Blackmagic Design\DaVinci Resolve\Resolve.exe"
        ],
        "folders": [
            r"C:\Users\Jordan\Videos\Projects"
        ],
        "web": [
            "https://www.youtube.com/studio/",
            "https://capcut.com/"
        ]
    }
}

def launch_mode(mode):
    if mode not in MODES:
        print(f"Mode '{mode}' not found.")
        return

    config = MODES[mode]

    print(f"Launching mode: {mode}")
    
    for app in config.get("apps", []):
        subprocess.Popen(app)
        time.sleep(1)  # Slight delay between launches

    for folder in config.get("folders", []):
        os.startfile(folder)

    for site in config.get("web", []):
        webbrowser.open(site)

    # Future: integrate FancyZones layout loader, AutoHotkey window arranger, etc.

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python WorkspaceModesLauncher.py [mode]")
    else:
        launch_mode(sys.argv[1])
