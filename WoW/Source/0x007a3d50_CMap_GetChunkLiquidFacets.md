---
offset: "0x007a3d50"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a3d50 — `CMap_GetChunkLiquidFacets`

- **Адрес (Offset):** `0x007a3d50`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a3d50
bool CMap::GetChunkLiquidFacets(CMapChunk* chunk, CWFrustum* frustum, CiRect* rect, CChunkLiquid* liquid, World::FacetData* facets) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a3d50 в IDA Pro / Ghidra
