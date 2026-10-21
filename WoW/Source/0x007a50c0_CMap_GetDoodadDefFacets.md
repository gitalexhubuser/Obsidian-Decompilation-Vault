---
offset: "0x007a50c0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a50c0 — `CMap_GetDoodadDefFacets`

- **Адрес (Offset):** `0x007a50c0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a50c0
bool CMap::GetDoodadDefFacets(TSList<CMapBaseObjLink, TSGetExplicitLink<CMapBaseObjLink> >* linkList, CAaBox* box, World::FacetData* facets, uint32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a50c0 в IDA Pro / Ghidra
