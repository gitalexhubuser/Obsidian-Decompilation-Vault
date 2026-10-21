---
offset: "0x007a7cc0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObj.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a7cc0 — `CMapObj_BuildLiquidVerts`

- **Адрес (Offset):** `0x007a7cc0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObj.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a7cc0
uint16_t CMapObj::BuildLiquidVerts(CMapObjGroup* group, const C44Matrix& matrix, const CImVector* color, int32_t magma, float texCoord1U, const TSGrowableArray<uint8_t>* sharedVerts, uint32_t stride, C3Vector** position, C3Vector** normal, CImVector** vertexColor, C2Vector** texCoord0, C2Vector** texCoord1) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a7cc0 в IDA Pro / Ghidra
