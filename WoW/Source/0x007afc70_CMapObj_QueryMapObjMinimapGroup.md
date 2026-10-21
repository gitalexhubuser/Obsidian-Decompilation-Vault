---
offset: "0x007afc70"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObj.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007afc70 — `CMapObj_QueryMapObjMinimapGroup`

- **Адрес (Offset):** `0x007afc70`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObj.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007afc70
void CMapObj::QueryMapObjMinimapGroup(int32_t groupNum, int32_t fromGroup, CAaBox* box, TSStackArray<MINIMAPQUADINFO>* quads, uint32_t maxQuads, int32_t inside, uint32_t flagsMask, uint32_t depth) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007afc70 в IDA Pro / Ghidra
