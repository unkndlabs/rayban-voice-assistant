# Setup Notes (April 2025)

## 1  Whisper.cpp GPU build on Windows

1. **Clone as submodule**

   ```git submodule add https://github.com/ggerganov/whisper.cpp```

2. **Patch CUDA toolset (if MSBuild fails)**
    Copy from
    `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6\MSBuildExtensions\*`
    to
    `C:\Program Files\Microsoft Visual Studio\2022\BuildTools\MSBuild\Microsoft\VC\v170\BuildCustomizations\`

3. **Configure and build**
    ```
    rmdir /s /q build
    cmake -B build ^
      -DGGML_CUDA=1 ^
      -DCUDAToolkit_ROOT="C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v12.6" ^
      -DCMAKE_CUDA_COMPILER="C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v12.6/bin/nvcc.exe"
    cmake --build build --config Release
    ```

4. **Download model**
    ```
    cd whisper.cpp
    bash models/download-ggml-model.sh medium   # or large-v3
    ```

5. **Python deps**
    ```pip install requirements.txt```

6. **Configure paths**
    Create a file named **.env** in the repo root with two variables pointing at your compiled Whisper build and model:
    ```
    # example .env  ──────────────────────────────────────────
    WHISPER_CLI=C:\WorkspaceModes\whisper.cpp\build\bin\Release\whisper-cli.exe
    MODEL_PATH=C:\WorkspaceModes\whisper.cpp\models\ggml-medium.bin
    ```

7. **Pair Meta Ray-Ban glasses**
    Windows Settings → Bluetooth → Ray-Ban Meta → set as default input.

8. First functional test
    ```
    python scripts/record_and_transcribe.py
    ```