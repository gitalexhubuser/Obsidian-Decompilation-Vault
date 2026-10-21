---
offset: "0x00450ac0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Thread/Win64/Thread.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00450ac0 — `Thread_Create`

- **Адрес (Offset):** `0x00450ac0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Thread/Win64/Thread.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00450ac0
bool Blizzard::Thread::Create(uint32_t (*function)(void*), void* param, ThreadRecord** thread, const char* name, int32_t flags, int32_t stackSize) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00450ac0 в IDA Pro / Ghidra
