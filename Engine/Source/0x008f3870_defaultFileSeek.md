---
offset: "0x008f3870"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_codeci.h"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008f3870 — `defaultFileSeek`

- **Адрес (Offset):** `0x008f3870`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_codeci.h`

## Сигнатура C++
```cpp
// OFFSET: 0x008f3870
static FMOD_INLINE FMOD_RESULT F_CALLBACK defaultFileSeek     (void *handle, unsigned int pos, void *userdata) { return ((File *)handle)->seek(pos, SEEK_SET); }
```

## Исследование и заметки
- [ ] Открыть адрес 0x008f3870 в IDA Pro / Ghidra
