---
offset: "0x007a3570"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a3570 — `CMap_VectorIntersectSubChunkList`

- **Адрес (Offset):** `0x007a3570`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a3570
bool CMap::VectorIntersectSubChunkList(C3Vector* start, C3Vector* end, float* distance, uint32_t flags, CMapChunk** hitChunk) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a3570 в IDA Pro / Ghidra
