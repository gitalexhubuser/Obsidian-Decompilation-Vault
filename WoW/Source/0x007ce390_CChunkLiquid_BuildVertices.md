---
offset: "0x007ce390"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapChunkLiquid.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007ce390 — `CChunkLiquid_BuildVertices`

- **Адрес (Offset):** `0x007ce390`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapChunkLiquid.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007ce390
void CChunkLiquid::BuildVertices(const C44Matrix* transform, uint32_t stride, C3Vector** position, C3Vector** normal, uint32_t** color, C2Vector** texCoord1, C2Vector** texCoord0) const {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007ce390 в IDA Pro / Ghidra
