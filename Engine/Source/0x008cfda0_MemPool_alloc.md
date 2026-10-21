---
offset: "0x008cfda0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_memory.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008cfda0 — `MemPool_alloc`

- **Адрес (Offset):** `0x008cfda0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_memory.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008cfda0
void *MemPool::alloc(int len, const char *file, const int line, FMOD_MEMORY_TYPE type, bool clear)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008cfda0 в IDA Pro / Ghidra
