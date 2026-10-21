---
offset: "0x0075c5a0"
module: "WoW/Source"
file: "WoW/Source/Object/Movement.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0075c5a0 — `ClipMovementPyramid`

- **Адрес (Offset):** `0x0075c5a0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/Movement.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0075c5a0
static int32_t ClipMovementPyramid(World::FacetData* facets, const C3Vector& direction, const C4Plane* clipPlanes, uint32_t clipCount, const C4Plane* planes, uint32_t planeIndex, float* distance, uint32_t* facetIndex) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0075c5a0 в IDA Pro / Ghidra
