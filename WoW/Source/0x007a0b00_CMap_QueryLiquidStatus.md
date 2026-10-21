---
offset: "0x007a0b00"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a0b00 — `CMap_QueryLiquidStatus`

- **Адрес (Offset):** `0x007a0b00`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a0b00
bool CMap::QueryLiquidStatus(C3Vector* pos, int32_t* liquidType, float* height, int32_t* a4, int32_t checkGround) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a0b00 в IDA Pro / Ghidra
