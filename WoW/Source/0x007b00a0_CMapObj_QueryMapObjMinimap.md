---
offset: "0x007b00a0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObj.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007b00a0 — `CMapObj_QueryMapObjMinimap`

- **Адрес (Offset):** `0x007b00a0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObj.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007b00a0
bool CMapObj::QueryMapObjMinimap(int32_t groupNum, CAaBox* box, TSStackArray<MINIMAPQUADINFO>* quads, uint32_t maxQuads, int32_t inside, uint8_t indoorArea) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007b00a0 в IDA Pro / Ghidra
