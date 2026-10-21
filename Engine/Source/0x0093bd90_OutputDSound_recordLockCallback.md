---
offset: "0x0093bd90"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_dsound.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0093bd90 — `OutputDSound_recordLockCallback`

- **Адрес (Offset):** `0x0093bd90`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_dsound.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0093bd90
FMOD_RESULT F_CALLBACK OutputDSound::recordLockCallback(FMOD_OUTPUT_STATE *output, unsigned int offset, unsigned int length, void **ptr1, void **ptr2, unsigned int *len1, unsigned int *len2)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0093bd90 в IDA Pro / Ghidra
