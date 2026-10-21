---
offset: "0x004510a0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Thread/ThreadPools.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004510a0 — `Thread_CreateFromPool`

- **Адрес (Offset):** `0x004510a0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Thread/ThreadPools.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004510a0
bool Blizzard::Thread::CreateFromPool(ThreadPoolRecord* pool, uint32_t (*function)(void*), void* param, ThreadRecord** thread, int32_t flags, int32_t stackSize) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004510a0 в IDA Pro / Ghidra
