---
offset: "0x004f48e0"
module: "WoW/Source"
file: "WoW/Source/Object/Passenger.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004f48e0 — `CPassenger_CPassenger`

- **Адрес (Offset):** `0x004f48e0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/Passenger.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004f48e0
CPassenger::CPassenger(const WOWGUID& transportGuid, const C3Vector& position, const WOWGUID& ownerGuid) : m_transportGuid(transportGuid), m_position(position) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004f48e0 в IDA Pro / Ghidra
