---
offset: "0x00544140"
module: "WoW/Source"
file: "WoW/Source/Ui/WorldMap.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00544140 — `CGWorldMap_GetWorldPosition`

- **Адрес (Offset):** `0x00544140`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/WorldMap.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00544140
bool CGWorldMap::GetWorldPosition(const C3Vector& position, int32_t mapID, float* x, float* y, bool* outland, bool noClamp, int32_t dungeonMapID) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00544140 в IDA Pro / Ghidra
