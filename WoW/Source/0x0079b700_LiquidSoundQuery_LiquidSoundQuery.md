---
offset: "0x0079b700"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObjGroup.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0079b700 — `LiquidSoundQuery_LiquidSoundQuery`

- **Адрес (Offset):** `0x0079b700`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObjGroup.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0079b700
LiquidSoundQuery::LiquidSoundQuery(const C2iVector& size, SpanRange* spans, const C3Vector& position, int32_t liquidType, const SMOLTile* tiles, const SMOLiquidVert* verts, TSGrowableArray<World::LiquidQueryResult>* results) : SpanRasterizer(size, spans) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0079b700 в IDA Pro / Ghidra
