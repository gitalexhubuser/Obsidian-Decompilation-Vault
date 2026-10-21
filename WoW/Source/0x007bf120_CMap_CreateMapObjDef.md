---
offset: "0x007bf120"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007bf120 — `CMap_CreateMapObjDef`

- **Адрес (Offset):** `0x007bf120`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007bf120
CMapObjDef* CMap::CreateMapObjDef(const char* fileName, const C3Vector* position, float facing, int32_t waitLoad, uint32_t doodadSetCount, const int16_t* doodadSets, float* radius, uint32_t id) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007bf120 в IDA Pro / Ghidra
