---
offset: "0x0078ec70"
module: "WoW/Source"
file: "WoW/Source/WorldClient/AreaList.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0078ec70 — `AreaListUpdateCurrentZone`

- **Адрес (Offset):** `0x0078ec70`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/AreaList.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0078ec70
static bool AreaListUpdateCurrentZone(CMapEntity* entity, const char** zoneName, const char** subzoneName, int32_t wmoId, int32_t wmoHash, int32_t wmoGroupNum, int32_t areaId, const AreaTableRec* zone, const AreaTableRec* area) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0078ec70 в IDA Pro / Ghidra
