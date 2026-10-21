---
offset: "0x006fcb60"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitMissileTrajectory_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006fcb60 — `CMissileCollision_Init`

- **Адрес (Offset):** `0x006fcb60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitMissileTrajectory_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006fcb60
int32_t CMissileCollision::Init(const C3Vector* start, const C3Vector* end, float pitch, float speed, const SpellMissileRec* missile, CGUnit_C* caster) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006fcb60 в IDA Pro / Ghidra
