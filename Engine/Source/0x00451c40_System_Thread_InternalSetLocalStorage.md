---
offset: "0x00451c40"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Thread/Win64/Thread.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00451c40 — `System_Thread_InternalSetLocalStorage`

- **Адрес (Offset):** `0x00451c40`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Thread/Win64/Thread.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00451c40
void System_Thread::InternalSetLocalStorage(const Blizzard::Thread::TLSSlot* slot, const void* value) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00451c40 в IDA Pro / Ghidra
