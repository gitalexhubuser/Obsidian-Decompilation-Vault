---
offset: "0x0077f130"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0077f130 — `World_QueryMapObjMinimap`

- **Адрес (Offset):** `0x0077f130`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077f130
bool World::QueryMapObjMinimap(CMapEntity* entity, CAaBox* box, TSStackArray<MINIMAPQUADINFO>* quads, uint32_t maxQuads, int32_t inside, uint8_t indoorArea) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077f130 в IDA Pro / Ghidra
