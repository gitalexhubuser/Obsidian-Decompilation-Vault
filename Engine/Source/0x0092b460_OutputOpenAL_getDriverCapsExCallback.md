---
offset: "0x0092b460"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_openal.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0092b460 — `OutputOpenAL_getDriverCapsExCallback`

- **Адрес (Offset):** `0x0092b460`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_openal.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0092b460
FMOD_RESULT OutputOpenAL::getDriverCapsExCallback(FMOD_OUTPUT_STATE *output, int id, FMOD_CAPS *caps, int *minfrequency, int *maxfrequency, FMOD_SPEAKERMODE *controlpanelspeakermode, int *num2dchannels, int *num3dchannels, int *totalchannels)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0092b460 в IDA Pro / Ghidra
