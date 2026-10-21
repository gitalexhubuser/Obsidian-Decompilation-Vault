---
offset: "0x006ebd30"
module: "WoW/Source"
file: "WoW/Source/Object/Movement.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006ebd30 — `CMovement_C_CMovement_C`

- **Адрес (Offset):** `0x006ebd30`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/Movement.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006ebd30
CMovement_C::CMovement_C(const C3Vector& position, float facing, const WOWGUID& ownerGuid, CGUnit_C* unit) : CMovementShared(WOWGUID(), position, facing, ownerGuid) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006ebd30 в IDA Pro / Ghidra
