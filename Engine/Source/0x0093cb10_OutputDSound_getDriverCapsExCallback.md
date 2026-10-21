---
offset: "0x0093cb10"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_dsound.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0093cb10 — `OutputDSound_getDriverCapsExCallback`

- **Адрес (Offset):** `0x0093cb10`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_dsound.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0093cb10
FMOD_RESULT OutputDSound::getDriverCapsExCallback(FMOD_OUTPUT_STATE *output, int id, FMOD_CAPS *caps, int *minfrequency, int *maxfrequency, FMOD_SPEAKERMODE *controlpanelspeakermode, int *num2dchannels, int *num3dchannels, int *totalchannels)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0093cb10 в IDA Pro / Ghidra
