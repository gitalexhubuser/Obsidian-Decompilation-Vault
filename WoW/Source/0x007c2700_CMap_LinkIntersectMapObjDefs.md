---
offset: "0x007c2700"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007c2700 — `CMap_LinkIntersectMapObjDefs`

- **Адрес (Offset):** `0x007c2700`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007c2700
bool CMap::LinkIntersectMapObjDefs(C3Vector& start, C3Vector& end, C3Vector& mid, MapObjIntersectData* interiorHit, MapObjIntersectData* groundHit, CMapChunk* chunk) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007c2700 в IDA Pro / Ghidra
