---
offset: "0x007aecb0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObj.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007aecb0 — `CMapObj_VectorIntersect`

- **Адрес (Offset):** `0x007aecb0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObj.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007aecb0
bool CMapObj::VectorIntersect(C3Vector& start, C3Vector& end, uint32_t flags, uint32_t groupIgnoreFlags, float* t, uint16_t* hitFace, CMapObjDef* mapObjDef, float* normalDot, uint32_t* hitGroup) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007aecb0 в IDA Pro / Ghidra
