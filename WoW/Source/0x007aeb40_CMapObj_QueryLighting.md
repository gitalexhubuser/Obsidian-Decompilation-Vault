---
offset: "0x007aeb40"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObj.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007aeb40 — `CMapObj_QueryLighting`

- **Адрес (Offset):** `0x007aeb40`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObj.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007aeb40
bool CMapObj::QueryLighting(uint32_t groupNum, const C3Vector& point, uint16_t face, CImVector* color, uint8_t* flag) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007aeb40 в IDA Pro / Ghidra
