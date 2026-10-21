---
offset: "0x00450d80"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Thread/Win64/ThreadPools.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00450d80 — `ThreadWorker_Start`

- **Адрес (Offset):** `0x00450d80`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Thread/Win64/ThreadPools.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00450d80
bool System_Thread::ThreadWorker::Start(Blizzard::Thread::ThreadPoolRecord* pool, int32_t flags, int32_t stackSize) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00450d80 в IDA Pro / Ghidra
