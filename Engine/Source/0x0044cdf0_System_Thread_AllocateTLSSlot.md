---
offset: "0x0044cdf0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Thread/Win64/Thread.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0044cdf0 — `System_Thread_AllocateTLSSlot`

- **Адрес (Offset):** `0x0044cdf0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Thread/Win64/Thread.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0044cdf0
bool System_Thread::AllocateTLSSlot(Blizzard::Thread::TLSSlot* slot, Blizzard::Thread::TLSDestructor destructor) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0044cdf0 в IDA Pro / Ghidra
