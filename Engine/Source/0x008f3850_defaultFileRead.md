---
offset: "0x008f3850"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_codeci.h"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008f3850 — `defaultFileRead`

- **Адрес (Offset):** `0x008f3850`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_codeci.h`

## Сигнатура C++
```cpp
// OFFSET: 0x008f3850
static FMOD_INLINE FMOD_RESULT F_CALLBACK defaultFileRead     (void *handle, void *buffer, unsigned int size, unsigned int *read, void *userdata) { return ((File *)handle)->read(buffer, 1, size, read); }
```

## Исследование и заметки
- [ ] Открыть адрес 0x008f3850 в IDA Pro / Ghidra
