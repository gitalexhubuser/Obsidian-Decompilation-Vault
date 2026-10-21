---
offset: "0x007a39f0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a39f0 — `CMap_VectorIntersectTerrain`

- **Адрес (Offset):** `0x007a39f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a39f0
bool CMap::VectorIntersectTerrain(C3Vector* start, C3Vector* end, float* distance, uint32_t flags, CMapChunk** hitChunk) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a39f0 в IDA Pro / Ghidra
