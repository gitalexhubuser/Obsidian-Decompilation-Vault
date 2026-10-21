---
offset: "0x007c1ad0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapLoad.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007c1ad0 — `CMapStaticEntity_AdjustLightmap`

- **Адрес (Offset):** `0x007c1ad0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapLoad.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007c1ad0
void CMapStaticEntity::AdjustLightmap(const CImVector* color, CImVector* diffuse, CImVector limit, CImVector* ambient, uint8_t maxBrightness) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007c1ad0 в IDA Pro / Ghidra
