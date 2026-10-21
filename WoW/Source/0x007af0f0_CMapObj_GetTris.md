---
offset: "0x007af0f0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObj.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007af0f0 — `CMapObj_GetTris`

- **Адрес (Offset):** `0x007af0f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObj.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007af0f0
bool CMapObj::GetTris(const CWFrustum& frustum, uint32_t flags, World::TriData* triData, CMapObjDef* mapObjDef) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007af0f0 в IDA Pro / Ghidra
