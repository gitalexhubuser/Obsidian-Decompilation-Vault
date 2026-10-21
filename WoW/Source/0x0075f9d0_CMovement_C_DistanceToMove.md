---
offset: "0x0075f9d0"
module: "WoW/Source"
file: "WoW/Source/Object/Movement.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0075f9d0 — `CMovement_C_DistanceToMove`

- **Адрес (Offset):** `0x0075f9d0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/Movement.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0075f9d0
int32_t CMovement_C::DistanceToMove(World::FacetData* facets, const C3Vector& direction, float distance, uint32_t* facetIndex, C4Plane* planes, uint32_t* planeCount, float* moveDistance, const C3Vector* position) const {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0075f9d0 в IDA Pro / Ghidra
