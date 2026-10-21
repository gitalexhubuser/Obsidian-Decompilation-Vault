---
offset: "0x009c25d0"
module: "WoW/Source"
file: "WoW/Source/Battlenet/Tumor/CreepTendril.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x009c25d0 — `Instance_Instance`

- **Адрес (Offset):** `0x009c25d0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/Tumor/CreepTendril.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009c25d0
Battlenet::CreepTendril::Instance::Instance(const Authentication::Settings& settings, TumorManager& manager) : Tendril(Battlenet::Event::CREEP, manager) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x009c25d0 в IDA Pro / Ghidra
