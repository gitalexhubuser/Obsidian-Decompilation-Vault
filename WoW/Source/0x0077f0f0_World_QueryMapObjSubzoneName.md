---
offset: "0x0077f0f0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0077f0f0 — `World_QueryMapObjSubzoneName`

- **Адрес (Offset):** `0x0077f0f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077f0f0
int32_t World::QueryMapObjSubzoneName(CMapEntity* entity, const char** subzoneName, int32_t* areaId) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077f0f0 в IDA Pro / Ghidra
