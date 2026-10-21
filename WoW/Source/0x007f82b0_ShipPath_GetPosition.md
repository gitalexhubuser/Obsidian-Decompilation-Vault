---
offset: "0x007f82b0"
module: "WoW/Source"
file: "WoW/Source/Game/ShipPath.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007f82b0 — `ShipPath_GetPosition`

- **Адрес (Offset):** `0x007f82b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Game/ShipPath.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007f82b0
void ShipPath::GetPosition(uint32_t time, uint32_t elapsed, int32_t* mapId, uint32_t* sequence, C3Vector* position, float* facing, uint32_t* leg, float* roll, float* pitch, int32_t absolute) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007f82b0 в IDA Pro / Ghidra
