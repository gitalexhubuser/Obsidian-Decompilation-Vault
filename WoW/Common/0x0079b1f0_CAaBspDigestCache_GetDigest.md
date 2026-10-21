---
offset: "0x0079b1f0"
module: "WoW/Common"
file: "WoW/Common/AaBsp.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_common
---

# 0x0079b1f0 — `CAaBspDigestCache_GetDigest`

- **Адрес (Offset):** `0x0079b1f0`
- **Модуль:** `WoW/Common`
- **Файл исходника:** `WoW/Common/AaBsp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0079b1f0
CAaBspNodeDigest* CAaBspDigestCache::GetDigest(const CAaBsp& bsp, const CAaBspNode* node, SMOPoly* faces, const C3Vector* vertices, const uint16_t* faceVertexIndices) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0079b1f0 в IDA Pro / Ghidra
