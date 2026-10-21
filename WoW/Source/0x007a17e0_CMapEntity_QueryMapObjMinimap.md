---
offset: "0x007a17e0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapEntity.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a17e0 — `CMapEntity_QueryMapObjMinimap`

- **Адрес (Offset):** `0x007a17e0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapEntity.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a17e0
bool CMapEntity::QueryMapObjMinimap(CAaBox* box, TSStackArray<MINIMAPQUADINFO>* quads, uint32_t maxQuads, int32_t inside, uint8_t indoorArea) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a17e0 в IDA Pro / Ghidra
