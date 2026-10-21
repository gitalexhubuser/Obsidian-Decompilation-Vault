---
offset: "0x007af8d0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObj.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007af8d0 — `GetMinimapQuads`

- **Адрес (Offset):** `0x007af8d0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObj.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007af8d0
static void GetMinimapQuads(const CAaBox* bounds, const CAaBox* box, int32_t groupId, TSStackArray<MINIMAPQUADINFO>* quads, uint32_t maxQuads) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007af8d0 в IDA Pro / Ghidra
