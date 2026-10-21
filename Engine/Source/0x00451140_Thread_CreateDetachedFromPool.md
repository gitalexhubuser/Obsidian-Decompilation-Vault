---
offset: "0x00451140"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Thread/ThreadPools.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00451140 — `Thread_CreateDetachedFromPool`

- **Адрес (Offset):** `0x00451140`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Thread/ThreadPools.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00451140
bool Blizzard::Thread::CreateDetachedFromPool(ThreadPoolRecord* pool, uint32_t (*function)(void*), void* param, int32_t flags, int32_t stackSize) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00451140 в IDA Pro / Ghidra
