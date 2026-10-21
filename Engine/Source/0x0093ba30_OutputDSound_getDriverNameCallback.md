---
offset: "0x0093ba30"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_dsound.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0093ba30 — `OutputDSound_getDriverNameCallback`

- **Адрес (Offset):** `0x0093ba30`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_dsound.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0093ba30
FMOD_RESULT F_CALLBACK OutputDSound::getDriverNameCallback(FMOD_OUTPUT_STATE *output, int id, char *name, int namelen)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0093ba30 в IDA Pro / Ghidra
