---
offset: "0x00453720"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Thread/Win64/ThreadLocalStorage.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00453720 — `Thread_RegisterLocalStorage`

- **Адрес (Offset):** `0x00453720`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Thread/Win64/ThreadLocalStorage.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00453720
void* Blizzard::Thread::RegisterLocalStorage(TLSSlot* slot, void* (*constructor)(void*), void* param, TLSDestructor destructor) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00453720 в IDA Pro / Ghidra
