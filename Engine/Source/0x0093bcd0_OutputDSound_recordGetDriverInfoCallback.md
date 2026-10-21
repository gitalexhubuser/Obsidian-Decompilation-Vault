---
offset: "0x0093bcd0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_dsound.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0093bcd0 — `OutputDSound_recordGetDriverInfoCallback`

- **Адрес (Offset):** `0x0093bcd0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_dsound.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0093bcd0
FMOD_RESULT F_CALLBACK OutputDSound::recordGetDriverInfoCallback(FMOD_OUTPUT_STATE *output, int id, char *name, int namelen)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0093bcd0 в IDA Pro / Ghidra
