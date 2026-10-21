---
offset: "0x007a5330"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a5330 — `CMap_GetChunkFacets`

- **Адрес (Offset):** `0x007a5330`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a5330
bool CMap::GetChunkFacets(int32_t chunkX, int32_t chunkY, CiRect* subRect, CFrustum* frustum, World::FacetData* facets, uint32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a5330 в IDA Pro / Ghidra
