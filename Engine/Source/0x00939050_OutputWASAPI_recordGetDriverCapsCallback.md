---
offset: "0x00939050"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_wasapi.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00939050 — `OutputWASAPI_recordGetDriverCapsCallback`

- **Адрес (Offset):** `0x00939050`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_wasapi.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00939050
FMOD_RESULT F_CALLBACK OutputWASAPI::recordGetDriverCapsCallback(FMOD_OUTPUT_STATE *output, int id, FMOD_CAPS *caps, int *minfrequency, int *maxfrequency)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00939050 в IDA Pro / Ghidra
