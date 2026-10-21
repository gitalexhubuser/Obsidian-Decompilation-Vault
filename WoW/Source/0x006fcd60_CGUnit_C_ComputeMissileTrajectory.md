---
offset: "0x006fcd60"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitMissileTrajectory_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006fcd60 — `CGUnit_C_ComputeMissileTrajectory`

- **Адрес (Offset):** `0x006fcd60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitMissileTrajectory_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006fcd60
int32_t CGUnit_C::ComputeMissileTrajectory(const SpellRec* spell, float* pitch, float* speed, C3Vector* launch, C3Vector* impact, float* time, C3Vector* points, uint32_t* count, int32_t preview) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006fcd60 в IDA Pro / Ghidra
