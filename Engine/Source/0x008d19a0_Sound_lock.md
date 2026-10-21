---
offset: "0x008d19a0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_sound.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008d19a0 — `Sound_lock`

- **Адрес (Offset):** `0x008d19a0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_sound.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008d19a0
FMOD_RESULT Sound::lock(unsigned int offset, unsigned int length, void **ptr1, void **ptr2, unsigned int *len1, unsigned int *len2)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008d19a0 в IDA Pro / Ghidra
