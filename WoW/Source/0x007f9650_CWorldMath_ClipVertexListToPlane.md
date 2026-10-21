---
offset: "0x007f9650"
module: "WoW/Source"
file: "WoW/Source/WorldClient/CWorldMath.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007f9650 — `CWorldMath_ClipVertexListToPlane`

- **Адрес (Offset):** `0x007f9650`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/CWorldMath.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007f9650
void CWorldMath::ClipVertexListToPlane(const C3Vector* verts, uint32_t count, C3Vector* out, uint32_t& outCount, const C4Plane& plane, float epsilon, int32_t keepCoplanar) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007f9650 в IDA Pro / Ghidra
