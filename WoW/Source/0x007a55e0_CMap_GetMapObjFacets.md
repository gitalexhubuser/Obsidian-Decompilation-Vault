---
offset: "0x007a55e0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a55e0 — `CMap_GetMapObjFacets`

- **Адрес (Offset):** `0x007a55e0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a55e0
bool CMap::GetMapObjFacets(CAaBox* queryBox, CAaBox* box, World::FacetData* facets, uint32_t flags, uint32_t* status) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a55e0 в IDA Pro / Ghidra
