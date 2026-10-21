---
offset: "0x0093bc50"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_dsound.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0093bc50 — `OutputDSound_getSoundRAMCallback`

- **Адрес (Offset):** `0x0093bc50`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_dsound.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0093bc50
FMOD_RESULT F_CALLBACK OutputDSound::getSoundRAMCallback(FMOD_OUTPUT_STATE *output, int *currentalloced, int *maxalloced, int *total)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0093bc50 в IDA Pro / Ghidra
