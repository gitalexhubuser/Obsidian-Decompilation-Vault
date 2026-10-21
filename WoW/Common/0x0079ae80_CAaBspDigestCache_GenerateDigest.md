---
offset: "0x0079ae80"
module: "WoW/Common"
file: "WoW/Common/AaBsp.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_common
---

# 0x0079ae80 — `CAaBspDigestCache_GenerateDigest`

- **Адрес (Offset):** `0x0079ae80`
- **Модуль:** `WoW/Common`
- **Файл исходника:** `WoW/Common/AaBsp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0079ae80
void CAaBspDigestCache::GenerateDigest(CAaBspNodeDigest* digest, const CAaBsp& bsp, const CAaBspNode* node, SMOPoly* faces, const C3Vector* vertices, const uint16_t* faceVertexIndices) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0079ae80 в IDA Pro / Ghidra
