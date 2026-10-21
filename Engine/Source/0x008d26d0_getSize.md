---
offset: "0x008d26d0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_file.h"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008d26d0 — `getSize`

- **Адрес (Offset):** `0x008d26d0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_file.h`

## Сигнатура C++
```cpp
// OFFSET: 0x008d26d0
virtual FMOD_RESULT     getSize(unsigned int *size) { *size = mLength; return FMOD_OK; }
```

## Исследование и заметки
- [ ] Открыть адрес 0x008d26d0 в IDA Pro / Ghidra
