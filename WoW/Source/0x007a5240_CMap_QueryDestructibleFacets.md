---
offset: "0x007a5240"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a5240 — `CMap_QueryDestructibleFacets`

- **Адрес (Offset):** `0x007a5240`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a5240
void CMap::QueryDestructibleFacets(TSList<CMapBaseObjLink, TSGetExplicitLink<CMapBaseObjLink> >* list, CAaBox* box, World::FacetData* facets, uint32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a5240 в IDA Pro / Ghidra
