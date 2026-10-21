---
offset: "0x007c7230"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObjGroup.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007c7230 — `GetFaceIndicesUsingCache`

- **Адрес (Offset):** `0x007c7230`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObjGroup.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007c7230
template <> bool BspQuery_Volume<CAaBox>::GetFaceIndicesUsingCache(const CAaBsp& aaBsp, const CAaBspNode* node) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007c7230 в IDA Pro / Ghidra
