---
offset: "0x0093a360"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_winmm.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0093a360 — `OutputWinMM_lockCallback`

- **Адрес (Offset):** `0x0093a360`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_winmm.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0093a360
FMOD_RESULT F_CALLBACK OutputWinMM::lockCallback(FMOD_OUTPUT_STATE *output, unsigned int offset, unsigned int length, void **ptr1, void **ptr2, unsigned int *len1, unsigned int *len2)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0093a360 в IDA Pro / Ghidra
