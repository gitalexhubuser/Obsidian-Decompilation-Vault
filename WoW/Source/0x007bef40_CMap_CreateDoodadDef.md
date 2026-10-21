---
offset: "0x007bef40"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007bef40 — `CMap_CreateDoodadDef`

- **Адрес (Offset):** `0x007bef40`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007bef40
CMapDoodadDef* CMap::CreateDoodadDef(uint32_t doodadRef, SMODoodadDef* doodadDef, char* name, uint32_t key, C44Matrix* mat, uint16_t doodadSet) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007bef40 в IDA Pro / Ghidra
