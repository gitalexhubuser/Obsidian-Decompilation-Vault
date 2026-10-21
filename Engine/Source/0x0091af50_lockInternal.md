---
offset: "0x0091af50"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_sound_sample.h"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0091af50 — `lockInternal`

- **Адрес (Offset):** `0x0091af50`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_sound_sample.h`

## Сигнатура C++
```cpp
// OFFSET: 0x0091af50
virtual FMOD_RESULT  lockInternal(unsigned int offset, unsigned int length, void **ptr1, void **ptr2, unsigned int *len1, unsigned int *len2) { return FMOD_ERR_SUBSOUNDS; }
```

## Исследование и заметки
- [ ] Открыть адрес 0x0091af50 в IDA Pro / Ghidra
