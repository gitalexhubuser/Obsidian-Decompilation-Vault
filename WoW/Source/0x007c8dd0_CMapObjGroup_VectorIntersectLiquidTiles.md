---
offset: "0x007c8dd0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObjGroup.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007c8dd0 — `CMapObjGroup_VectorIntersectLiquidTiles`

- **Адрес (Offset):** `0x007c8dd0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObjGroup.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007c8dd0
bool CMapObjGroup::VectorIntersectLiquidTiles(const C3Segment& seg, float* t, uint32_t flags, uint32_t* tileCount, uint8_t* tiles, World::TriData* triData, CMapObjDef* mapObjDef) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007c8dd0 в IDA Pro / Ghidra
