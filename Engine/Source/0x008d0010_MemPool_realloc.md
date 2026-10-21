---
offset: "0x008d0010"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_memory.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008d0010 — `MemPool_realloc`

- **Адрес (Offset):** `0x008d0010`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_memory.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008d0010
void *MemPool::realloc(void *ptr, int len, const char *file, const int line, FMOD_MEMORY_TYPE type)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008d0010 в IDA Pro / Ghidra
