# glasses_voice_commands.py

import sounddevice as sd
import soundfile as sf
import subprocess
import time
import os

# --------------- CONFIGURATION ---------------- #
WHISPER_CLI = r"C:\WorkspaceModes\whisper.cpp\build\bin\Release\whisper-cli.exe"
MODEL_PATH = r"C:\WorkspaceModes\whisper.cpp\models\ggml-medium.bin"
RECORD_SECONDS = 3
SAMPLE_RATE = 16000
CHANNELS = 1
FILENAME = "input.wav"

# Define your voice commands here
COMMANDS = {
    "open notion": lambda: subprocess.Popen(["notion"]),
    "open blender": lambda: subprocess.Popen([r"C:\Program Files\Blender Foundation\Blender 4.2\blender-launcher.exe"]),
    "launch 3d mode": lambda: subprocess.run(["python", "WorkspaceModesLauncher.py", "3d"]),
    "open fusion": lambda: subprocess.Popen([r"C:\Users\Jordan\AppData\Local\Autodesk\webdeploy\production\6a0c9611291d45bb9226980209917c3d\FusionLauncher.exe"]),
}

# ------------------------------------------------ #

def record_audio():
    print("\n🎙️ Recording...")
    audio = sd.rec(int(RECORD_SECONDS * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=CHANNELS, dtype='float32')
    sd.wait()
    sf.write(FILENAME, audio, SAMPLE_RATE)
    print(f"✅ Recording saved to {FILENAME}")

def transcribe_audio():
    print("🔎 Transcribing...")
    result = subprocess.run([
        WHISPER_CLI,
        "--model", MODEL_PATH,
        "--file", FILENAME,
        "--split-on-word",
        "--beam-size", "5",
        "temperature", "0"
    ], capture_output=True, text=True)
    output = result.stdout
    lines = output.splitlines()
    transcript_lines = [line for line in lines if '-->' in line]
    if not transcript_lines:
        return ""
    last_line = transcript_lines[-1]
    parts = last_line.split(']')
    if len(parts) < 2:
        return ""
    transcript = parts[1].strip()
    print(f"📝 Transcript: '{transcript}'")
    return transcript.lower()

def match_and_execute(transcript):
    for command, action in COMMANDS.items():
        if command in transcript:
            print(f"✅ Matched command: {command}")
            action()
            return
    print("⚡ No matching command found.")

def main_loop():
    print("💬 Press Enter to listen. Say a command like 'open notion'...")
    while True:
        input("\n🔵 Press Enter to start recording...")
        record_audio()
        time.sleep(1)
        transcript = transcribe_audio()
        if transcript:
            match_and_execute(transcript)
        else:
            print("⚡ No speech detected.")
        time.sleep(1)

if __name__ == "__main__":
    main_loop()
