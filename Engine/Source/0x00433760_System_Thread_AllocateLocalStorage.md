---
offset: "0x00433760"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Thread/Win64/ThreadLocalStorage.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00433760 — `System_Thread_AllocateLocalStorage`

- **Адрес (Offset):** `0x00433760`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Thread/Win64/ThreadLocalStorage.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00433760
bool System_Thread::AllocateLocalStorage(Blizzard::Thread::TLSSlot* slot, Blizzard::Thread::TLSDestructor destructor) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00433760 в IDA Pro / Ghidra
