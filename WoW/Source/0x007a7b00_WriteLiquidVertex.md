---
offset: "0x007a7b00"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObj.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a7b00 — `WriteLiquidVertex`

- **Адрес (Offset):** `0x007a7b00`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObj.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a7b00
static void __stdcall WriteLiquidVertex(CMapObjGroup* group, const C44Matrix& matrix, const C3Vector& vertex, const SMOLiquidVert* liquidVert, const CImVector* color, int32_t magma, float texCoord1U, int32_t* unused, uint32_t stride, C3Vector** position, C3Vector** normal, CImVector** vertexColor, C2Vector** texCoord0, C2Vector** texCoord1) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a7b00 в IDA Pro / Ghidra
