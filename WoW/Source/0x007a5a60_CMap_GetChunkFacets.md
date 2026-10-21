---
offset: "0x007a5a60"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a5a60 — `CMap_GetChunkFacets`

- **Адрес (Offset):** `0x007a5a60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a5a60
bool CMap::GetChunkFacets(int32_t chunkX, int32_t chunkY, CiRect* subRect, CAaBox* queryBox, CAaBox* box, World::FacetData* facets, uint32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a5a60 в IDA Pro / Ghidra
