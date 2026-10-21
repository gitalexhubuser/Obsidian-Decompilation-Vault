---
offset: "0x00799980"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00799980 — `CWorldScene_CullDoodadsExterior`

- **Адрес (Offset):** `0x00799980`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00799980
void CWorldScene::CullDoodadsExterior(TSList<CMapBaseObjLink, TSGetExplicitLink<CMapBaseObjLink> >* linkList, uint8_t fadeLevel) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00799980 в IDA Pro / Ghidra
