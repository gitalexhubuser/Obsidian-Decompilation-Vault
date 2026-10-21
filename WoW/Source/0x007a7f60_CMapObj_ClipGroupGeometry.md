---
offset: "0x007a7f60"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObj.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a7f60 — `CMapObj_ClipGroupGeometry`

- **Адрес (Offset):** `0x007a7f60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObj.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a7f60
uint16_t CMapObj::ClipGroupGeometry(CMapObjGroup* group, const C44Matrix& matrix, const CImVector* color, int32_t magma, float texCoord1U, uint32_t stride, C3Vector** position, C3Vector** normal, CImVector** vertexColor, C2Vector** texCoord0, C2Vector** texCoord1, uint16_t** indices, uint16_t baseVertex) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a7f60 в IDA Pro / Ghidra
