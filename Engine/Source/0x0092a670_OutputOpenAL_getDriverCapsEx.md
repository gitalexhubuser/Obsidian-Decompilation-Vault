---
offset: "0x0092a670"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_openal.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0092a670 — `OutputOpenAL_getDriverCapsEx`

- **Адрес (Offset):** `0x0092a670`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_openal.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0092a670
FMOD_RESULT OutputOpenAL::getDriverCapsEx(int id, FMOD_CAPS *caps, int *minfrequency, int *maxfrequency, FMOD_SPEAKERMODE *controlpanelspeakermode, int *num2dchannels, int *num3dchannels, int *totalchannels)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0092a670 в IDA Pro / Ghidra
