---
offset: "0x007cb180"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObjGroup.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007cb180 — `CMapObjGroup_GetTris`

- **Адрес (Offset):** `0x007cb180`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObjGroup.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007cb180
bool CMapObjGroup::GetTris(const CWFrustum& frustum, uint32_t flags, uint16_t faceIgnoreFlags, World::TriData* triData, CMapObjDef* mapObjDef) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007cb180 в IDA Pro / Ghidra
