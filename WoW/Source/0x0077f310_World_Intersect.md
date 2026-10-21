---
offset: "0x0077f310"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0077f310 — `World_Intersect`

- **Адрес (Offset):** `0x0077f310`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077f310
int32_t World::Intersect(const C3Vector& start, const C3Vector& end, C3Vector* hit, float* distance, uint32_t flags, HitTestDebug* debug) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077f310 в IDA Pro / Ghidra
