---
offset: "0x00937240"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_asio.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00937240 — `OutputASIO_recordLockCallback`

- **Адрес (Offset):** `0x00937240`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_asio.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00937240
FMOD_RESULT F_CALLBACK OutputASIO::recordLockCallback(FMOD_OUTPUT_STATE *output, unsigned int offset, unsigned int length, void **ptr1, void **ptr2, unsigned int *len1, unsigned int *len2)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00937240 в IDA Pro / Ghidra
