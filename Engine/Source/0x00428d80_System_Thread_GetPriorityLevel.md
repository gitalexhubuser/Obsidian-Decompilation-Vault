---
offset: "0x00428d80"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Thread/Win64/Thread.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00428d80 — `System_Thread_GetPriorityLevel`

- **Адрес (Offset):** `0x00428d80`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Thread/Win64/Thread.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00428d80
bool System_Thread::GetPriorityLevel(Blizzard::Thread::ThreadRecord* thread, int32_t* level) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00428d80 в IDA Pro / Ghidra
