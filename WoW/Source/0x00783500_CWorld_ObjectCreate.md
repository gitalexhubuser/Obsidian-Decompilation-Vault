---
offset: "0x00783500"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00783500 — `CWorld_ObjectCreate`

- **Адрес (Offset):** `0x00783500`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00783500
CMapBaseObj* CWorld::ObjectCreate(const char* name, const C3Vector& position, float facing, int32_t waitLoad, int32_t snap, uint64_t guid, uint32_t doodadSetCount, const int16_t* doodadSets, float* radius, uint32_t id) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00783500 в IDA Pro / Ghidra
