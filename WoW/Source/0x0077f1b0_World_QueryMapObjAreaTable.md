---
offset: "0x0077f1b0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0077f1b0 — `World_QueryMapObjAreaTable`

- **Адрес (Offset):** `0x0077f1b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077f1b0
bool World::QueryMapObjAreaTable(CMapEntity* entity, WMOAreaTableRec** groupRec, WMOAreaTableRec** rootRec, int32_t* wmoGroupId) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077f1b0 в IDA Pro / Ghidra
