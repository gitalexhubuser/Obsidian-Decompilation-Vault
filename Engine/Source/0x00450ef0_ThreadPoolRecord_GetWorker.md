---
offset: "0x00450ef0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Thread/ThreadPools.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00450ef0 — `ThreadPoolRecord_GetWorker`

- **Адрес (Offset):** `0x00450ef0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Thread/ThreadPools.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00450ef0
System_Thread::ThreadWorker* Blizzard::Thread::ThreadPoolRecord::GetWorker(int32_t flags, int32_t stackSize) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00450ef0 в IDA Pro / Ghidra
