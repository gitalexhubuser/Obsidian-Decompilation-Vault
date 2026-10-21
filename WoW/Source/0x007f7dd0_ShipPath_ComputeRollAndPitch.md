---
offset: "0x007f7dd0"
module: "WoW/Source"
file: "WoW/Source/Game/ShipPath.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007f7dd0 — `ShipPath_ComputeRollAndPitch`

- **Адрес (Offset):** `0x007f7dd0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Game/ShipPath.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007f7dd0
void ShipPath::ComputeRollAndPitch(float speed, float facing, float distance, uint32_t leg, float turn, uint32_t time, C3Vector* position, float* roll, float* pitch) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007f7dd0 в IDA Pro / Ghidra
