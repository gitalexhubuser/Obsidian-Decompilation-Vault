---
offset: "0x007d59b0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007d59b0 — `CMap_LocateViewerMapObjs`

- **Адрес (Offset):** `0x007d59b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007d59b0
bool CMap::LocateViewerMapObjs(C3Vector& start, C3Vector& end, float dist, CMapObjDef** outDefs, uint32_t* outGroups) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007d59b0 в IDA Pro / Ghidra
