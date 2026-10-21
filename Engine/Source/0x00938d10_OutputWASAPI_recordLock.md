---
offset: "0x00938d10"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_wasapi.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00938d10 — `OutputWASAPI_recordLock`

- **Адрес (Offset):** `0x00938d10`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_wasapi.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00938d10
FMOD_RESULT OutputWASAPI::recordLock(unsigned int offset, unsigned int length, void **ptr1, void **ptr2, unsigned int *len1, unsigned int *len2)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00938d10 в IDA Pro / Ghidra
