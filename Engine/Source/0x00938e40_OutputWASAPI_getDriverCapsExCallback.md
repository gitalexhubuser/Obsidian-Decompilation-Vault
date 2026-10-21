---
offset: "0x00938e40"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_wasapi.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00938e40 — `OutputWASAPI_getDriverCapsExCallback`

- **Адрес (Offset):** `0x00938e40`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_wasapi.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00938e40
FMOD_RESULT F_CALLBACK OutputWASAPI::getDriverCapsExCallback(FMOD_OUTPUT_STATE *output, int id, FMOD_CAPS *caps, int *minfrequency, int *maxfrequency, FMOD_SPEAKERMODE *controlpanelspeakermode)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00938e40 в IDA Pro / Ghidra
