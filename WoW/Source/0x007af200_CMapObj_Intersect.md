---
offset: "0x007af200"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObj.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007af200 — `CMapObj_Intersect`

- **Адрес (Offset):** `0x007af200`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObj.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007af200
bool CMapObj::Intersect(C3Vector& start, C3Vector& end, float* distance, uint32_t flags, uint32_t ignoreFlags, uint32_t groupNum, int32_t* hitIndex) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007af200 в IDA Pro / Ghidra
