---
offset: "0x007c28f0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007c28f0 — `CMap_LinkStaticEntity`

- **Адрес (Offset):** `0x007c28f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007c28f0
void CMap::LinkStaticEntity(CMapStaticEntity* entity, C3Vector& top, C3Vector& bottom, C3Vector& mid, int32_t& outInterior, int32_t& outHit, MapObjIntersectData* interiorHit, MapObjIntersectData* groundHit) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007c28f0 в IDA Pro / Ghidra
