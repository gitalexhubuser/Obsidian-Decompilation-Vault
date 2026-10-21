---
offset: "0x007a85e0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObj.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a85e0 — `CMapObj_TransformAndClipVerts`

- **Адрес (Offset):** `0x007a85e0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObj.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a85e0
uint32_t CMapObj::TransformAndClipVerts(uint32_t noOcclusion, C3Vector* verts, uint32_t vertCount, C3Vector& offset, C3Vector*& clippedVerts, uint32_t& clippedCount) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a85e0 в IDA Pro / Ghidra
