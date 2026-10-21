---
offset: "0x007a2aa0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a2aa0 — `CMap_QueryIntersectingModels`

- **Адрес (Offset):** `0x007a2aa0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a2aa0
uint32_t CMap::QueryIntersectingModels(CM2Model** models, uint32_t maxModels, const CAaBox& box, uint32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a2aa0 в IDA Pro / Ghidra
