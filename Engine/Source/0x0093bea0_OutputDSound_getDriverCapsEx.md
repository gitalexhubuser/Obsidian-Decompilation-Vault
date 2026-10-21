---
offset: "0x0093bea0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_dsound.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0093bea0 — `OutputDSound_getDriverCapsEx`

- **Адрес (Offset):** `0x0093bea0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_dsound.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0093bea0
FMOD_RESULT OutputDSound::getDriverCapsEx(int id, FMOD_CAPS *caps, int *minfrequency, int *maxfrequency, FMOD_SPEAKERMODE *controlpanelspeakermode, int *num2dchannels, int *num3dchannels, int *totalchannels)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0093bea0 в IDA Pro / Ghidra
