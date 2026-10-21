---
offset: "0x0075cd70"
module: "WoW/Source"
file: "WoW/Source/Object/Movement.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0075cd70 — `DistanceToMovePyramid`

- **Адрес (Offset):** `0x0075cd70`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/Movement.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0075cd70
static void __stdcall DistanceToMovePyramid(World::FacetData* facets, const C3Vector& direction, float distance, const C3Vector& move, const C4Plane* volumePlanes, const C3Vector* volumePoints, const uint8_t* volumeFaces, uint32_t* facetIndex, C4Plane* hitPlanes, uint32_t* hitCount, float* hitDistance) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0075cd70 в IDA Pro / Ghidra
