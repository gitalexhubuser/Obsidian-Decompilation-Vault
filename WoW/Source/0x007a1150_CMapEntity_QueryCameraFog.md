---
offset: "0x007a1150"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapEntity.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a1150 — `CMapEntity_QueryCameraFog`

- **Адрес (Offset):** `0x007a1150`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapEntity.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a1150
int32_t CMapEntity::QueryCameraFog(SMOFog* fog, CMapObjDef** mapObjDef, uint8_t* found, TSGrowableArray<uint32_t>** groups, float* distance) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a1150 в IDA Pro / Ghidra
