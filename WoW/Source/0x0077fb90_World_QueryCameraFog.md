---
offset: "0x0077fb90"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0077fb90 — `World_QueryCameraFog`

- **Адрес (Offset):** `0x0077fb90`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077fb90
int32_t World::QueryCameraFog(SMOFog* fog, CMapObjDef** mapObjDef, uint8_t* found, TSGrowableArray<uint32_t>** groups, float* distance) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077fb90 в IDA Pro / Ghidra
