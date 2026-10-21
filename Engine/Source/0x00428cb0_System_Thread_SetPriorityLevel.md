---
offset: "0x00428cb0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Thread/Win64/Thread.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00428cb0 — `System_Thread_SetPriorityLevel`

- **Адрес (Offset):** `0x00428cb0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Thread/Win64/Thread.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00428cb0
bool System_Thread::SetPriorityLevel(Blizzard::Thread::ThreadRecord* thread, int32_t level) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00428cb0 в IDA Pro / Ghidra
