---
offset: "0x007c9dd0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObjGroup.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007c9dd0 — `CMapObjGroup_VectorIntersectLiquid`

- **Адрес (Offset):** `0x007c9dd0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObjGroup.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007c9dd0
bool CMapObjGroup::VectorIntersectLiquid(const C3Segment& seg, float* t, uint32_t flags, World::TriData* triData, CMapObjDef* mapObjDef) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007c9dd0 в IDA Pro / Ghidra
