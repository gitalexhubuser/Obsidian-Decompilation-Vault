---
offset: "0x00914e00"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_output_nosound.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00914e00 — `OutputNoSound_lockCallback`

- **Адрес (Offset):** `0x00914e00`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_output_nosound.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00914e00
FMOD_RESULT F_CALLBACK OutputNoSound::lockCallback(FMOD_OUTPUT_STATE *output, unsigned int offset, unsigned int length, void **ptr1, void **ptr2, unsigned int *len1, unsigned int *len2)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00914e00 в IDA Pro / Ghidra
