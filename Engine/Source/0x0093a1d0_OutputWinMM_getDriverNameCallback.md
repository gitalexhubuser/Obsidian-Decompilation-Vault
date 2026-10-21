---
offset: "0x0093a1d0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_winmm.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0093a1d0 — `OutputWinMM_getDriverNameCallback`

- **Адрес (Offset):** `0x0093a1d0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_winmm.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0093a1d0
FMOD_RESULT F_CALLBACK OutputWinMM::getDriverNameCallback(FMOD_OUTPUT_STATE *output, int id, char *name, int namelen)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0093a1d0 в IDA Pro / Ghidra
