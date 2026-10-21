---
offset: "0x007ad3b0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007ad3b0 — `CMap_GetHeightTerrain`

- **Адрес (Offset):** `0x007ad3b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007ad3b0
bool CMap::GetHeightTerrain(CMapChunk* chunk, C3Vector& pos, int32_t cellX, int32_t cellY, float* outHeight) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007ad3b0 в IDA Pro / Ghidra
