# Glasses-Voice-Assistant 🕶️🎙️  
Local voice-to-desktop control using Meta Ray-Ban glasses, Whisper.cpp + CUDA, and Python automations.

## Why
- **Zero cloud latency / cost** – everything runs on-device (RTX 4080).
- **Hands-free workflow** – speak commands to launch “workspace modes”, apps, or scripts.
- **Hackable** – extend with VAD, hotword detection, or offline LLM intent parsing.

## Quick Start
```
git clone --recursive https://github.com/unkndlabs/glasses-voice-assistant.git
cd glasses-voice-assistant
pip install -r requirements.txt
configure paths WHISPER_CLI and MODEL_PATH in `.env` for compiled whisper build and model files
python scripts/glasses_voice_commands.py
```
Press Enter, speak e.g. “open notion”, watch the magic.

## Repo Layout
- **scripts/**                 one-off tests and the live command loop
- **launcher/**                WorkspaceModesLauncher + mode scripts
- **whisper.cpp/**             submodule (GPU-enabled build, models not tracked)
- **models/**                  .bin models (add manually or via LFS, .gitignore’d)
- **docs/**                    setup notes, roadmap, etc.

## Minimum Hardware / Software
- Windows 10/11, GPU with CUDA 12.x (tested on RTX 4080)
- Visual Studio 2022 Build Tools + CUDA build customizations
- Python 3.10+

## Current Commands
Phrase	Action
`open notion`	Launch Notion desktop app
`open blender`	Launch Blender
`open fusion`	Launch Fusion 360
`launch 3d mode`	Run WorkspaceModesLauncher → 3D mode

## License
MIT for this repo. Whisper.cpp retains its own MIT license.
