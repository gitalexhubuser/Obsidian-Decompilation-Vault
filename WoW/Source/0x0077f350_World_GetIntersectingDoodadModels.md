---
offset: "0x0077f350"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0077f350 — `World_GetIntersectingDoodadModels`

- **Адрес (Offset):** `0x0077f350`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077f350
uint32_t World::GetIntersectingDoodadModels(CM2Model** models, uint32_t maxModels, const CAaBox& box, uint32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077f350 в IDA Pro / Ghidra
