---
offset: "0x00793270"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00793270 — `CWorldScene_CullEntitysInterior`

- **Адрес (Offset):** `0x00793270`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00793270
void CWorldScene::CullEntitysInterior(TSList<CMapBaseObjLink, TSGetExplicitLink<CMapBaseObjLink> >* linkList, CWFrustum* frustum, int32_t force, int32_t interior) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00793270 в IDA Pro / Ghidra
