---
offset: "0x0098c580"
module: "WoW/Source"
file: "WoW/Source/Object/MovementShared.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0098c580 — `CMovementShared_CMovementShared`

- **Адрес (Offset):** `0x0098c580`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/MovementShared.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0098c580
CMovementShared::CMovementShared(const WOWGUID& transportGuid, const C3Vector& position, float facing, const WOWGUID& ownerGuid) : CPassenger(transportGuid, position, ownerGuid), m_groundNormal(0.0f, 0.0f, 1.0f), m_anchorPos(position) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0098c580 в IDA Pro / Ghidra
