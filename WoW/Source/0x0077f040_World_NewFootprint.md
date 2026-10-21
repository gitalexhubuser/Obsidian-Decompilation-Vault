---
offset: "0x0077f040"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0077f040 — `World_NewFootprint`

- **Адрес (Offset):** `0x0077f040`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077f040
void World::NewFootprint(int32_t textureId, const float* size, const C3Vector* position, float facing, int32_t left, int32_t terrainType, int32_t activePlayer) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077f040 в IDA Pro / Ghidra
