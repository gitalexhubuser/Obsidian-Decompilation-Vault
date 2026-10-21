---
offset: "0x008d0550"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008d0550 — `FMOD_Memory_Initialize`

- **Адрес (Offset):** `0x008d0550`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008d0550
FMOD_RESULT F_API FMOD_Memory_Initialize(void *poolmem, int poollen, FMOD_MEMORY_ALLOCCALLBACK useralloc, FMOD_MEMORY_REALLOCCALLBACK userrealloc, FMOD_MEMORY_FREECALLBACK userfree)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008d0550 в IDA Pro / Ghidra
