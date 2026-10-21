---
offset: "0x007a0820"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a0820 — `CMap_QueryLiquidTerrain`

- **Адрес (Offset):** `0x007a0820`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a0820
bool CMap::QueryLiquidTerrain(const C3Vector* pos, int32_t* liquidType, float* height, int32_t checkGround) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a0820 в IDA Pro / Ghidra
