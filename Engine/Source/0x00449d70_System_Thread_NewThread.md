---
offset: "0x00449d70"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Thread/Win64/Thread.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00449d70 — `System_Thread_NewThread`

- **Адрес (Offset):** `0x00449d70`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Thread/Win64/Thread.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00449d70
Blizzard::Thread::ThreadRecord* System_Thread::NewThread(uint32_t (*function)(void*), void* param, const char* name) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00449d70 в IDA Pro / Ghidra
