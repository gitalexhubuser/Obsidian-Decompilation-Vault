---
offset: "0x007beb40"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Map.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007beb40 — `CMap_CreateDoodadDef`

- **Адрес (Offset):** `0x007beb40`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Map.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007beb40
CMapDoodadDef* CMap::CreateDoodadDef(const char* fileName, const C3Vector* position, float facing, int32_t waitForLoad) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007beb40 в IDA Pro / Ghidra
