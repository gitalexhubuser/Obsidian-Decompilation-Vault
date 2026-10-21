---
offset: "0x007a3b70"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a3b70 — `CMap_Intersect`

- **Адрес (Offset):** `0x007a3b70`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a3b70
bool CMap::Intersect(C3Vector* start, C3Vector* end, C3Vector* hitPoint, float* distance, uint32_t flags, World::HitTestDebug* hitInfo) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a3b70 в IDA Pro / Ghidra
