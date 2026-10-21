---
offset: "0x0079bbf0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObj.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0079bbf0 — `CMapObj_QueryLiquidSounds`

- **Адрес (Offset):** `0x0079bbf0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObj.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0079bbf0
void CMapObj::QueryLiquidSounds(uint32_t groupIndex, uint32_t fromGroup, uint32_t depth, uint32_t* minDepth, const C3Vector& pos, TSGrowableArray<World::LiquidQueryResult>& results) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0079bbf0 в IDA Pro / Ghidra
