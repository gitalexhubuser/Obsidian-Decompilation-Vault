---
offset: "0x00450bf0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Thread/Win64/Thread.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00450bf0 — `System_Thread_RegisterExternalTLSDestructor`

- **Адрес (Offset):** `0x00450bf0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Thread/Win64/Thread.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00450bf0
void System_Thread::RegisterExternalTLSDestructor(void* value, Blizzard::Thread::TLSDestructor destructor) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00450bf0 в IDA Pro / Ghidra
