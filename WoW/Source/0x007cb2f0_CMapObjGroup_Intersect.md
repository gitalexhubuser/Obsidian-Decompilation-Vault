---
offset: "0x007cb2f0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObjGroup.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007cb2f0 — `CMapObjGroup_Intersect`

- **Адрес (Offset):** `0x007cb2f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObjGroup.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007cb2f0
bool CMapObjGroup::Intersect(C3Segment& seg, float* dist, uint32_t flags, uint16_t faceIgnoreFlags, int32_t* hitIndex) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007cb2f0 в IDA Pro / Ghidra
