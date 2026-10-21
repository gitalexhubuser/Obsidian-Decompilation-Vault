---
offset: "0x007d77c0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObj.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007d77c0 — `CMapObj_DistFromClosestExtPortal`

- **Адрес (Offset):** `0x007d77c0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObj.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007d77c0
void CMapObj::DistFromClosestExtPortal(uint32_t depth, uint32_t flags, CMapObjGroup* group, CMapObjGroup* fromGroup, const C3Vector& pos, float* dist) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007d77c0 в IDA Pro / Ghidra
