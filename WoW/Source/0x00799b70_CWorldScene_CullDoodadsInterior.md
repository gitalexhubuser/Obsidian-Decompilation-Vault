---
offset: "0x00799b70"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00799b70 — `CWorldScene_CullDoodadsInterior`

- **Адрес (Offset):** `0x00799b70`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00799b70
void CWorldScene::CullDoodadsInterior(TSList<CMapBaseObjLink, TSGetExplicitLink<CMapBaseObjLink> >* linkList, CWFrustum* frustum, uint16_t fadeLevel, int32_t interior) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00799b70 в IDA Pro / Ghidra
