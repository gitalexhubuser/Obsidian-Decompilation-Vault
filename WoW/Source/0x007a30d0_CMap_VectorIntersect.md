---
offset: "0x007a30d0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a30d0 — `CMap_VectorIntersect`

- **Адрес (Offset):** `0x007a30d0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a30d0
bool CMap::VectorIntersect(C3Vector* start, C3Vector* end, uint32_t flags, uint32_t defIgnoreFlags, float* distance, uint16_t* hitIndex, CMapObj** outMapObj, CMapObjDef** outMapObjDef, CMapObjDefGroup** outMapObjDefGroup) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a30d0 в IDA Pro / Ghidra
