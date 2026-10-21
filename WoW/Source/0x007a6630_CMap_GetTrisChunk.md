---
offset: "0x007a6630"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a6630 — `CMap_GetTrisChunk`

- **Адрес (Offset):** `0x007a6630`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a6630
bool CMap::GetTrisChunk(int32_t chunkX, int32_t chunkY, const CiRect& cellRect, const CAaBox& box, World::TriData* triData, uint32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a6630 в IDA Pro / Ghidra
