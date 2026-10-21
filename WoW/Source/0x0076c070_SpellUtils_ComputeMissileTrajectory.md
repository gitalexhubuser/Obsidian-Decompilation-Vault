---
offset: "0x0076c070"
module: "WoW/Source"
file: "WoW/Source/Magic/Spell.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0076c070 — `SpellUtils_ComputeMissileTrajectory`

- **Адрес (Offset):** `0x0076c070`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/Spell.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0076c070
int32_t SpellUtils_ComputeMissileTrajectory(float pitch, const C3Vector* delta, float gravity, float* speed, float* time, C3Vector* velocity) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0076c070 в IDA Pro / Ghidra
