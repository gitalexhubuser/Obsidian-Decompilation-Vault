---
offset: "0x00428380"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Lock/Win64/Event.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00428380 — `Lock_EventWait`

- **Адрес (Offset):** `0x00428380`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Lock/Win64/Event.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00428380
Blizzard::Lock::Event* Blizzard::Lock::EventWait(uint32_t timeout, Event& event) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00428380 в IDA Pro / Ghidra
