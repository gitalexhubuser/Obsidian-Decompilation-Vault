---
offset: "0x00939080"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_wasapi.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00939080 — `OutputWASAPI_recordStartCallback`

- **Адрес (Offset):** `0x00939080`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_wasapi.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00939080
FMOD_RESULT F_CALLBACK OutputWASAPI::recordStartCallback(FMOD_OUTPUT_STATE *output, int id, FMOD_SOUND *sound, int loop)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00939080 в IDA Pro / Ghidra
