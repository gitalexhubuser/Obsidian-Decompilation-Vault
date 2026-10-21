---
offset: "0x0078cd30"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Snow.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0078cd30 — `Snow_Snow`

- **Адрес (Offset):** `0x0078cd30`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Snow.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0078cd30
Snow::Snow(float width, float height) : m_bbox(C3Vector(0.0f, 0.0f, 0.0f), C3Vector(0.0f, 0.0f, 0.0f)), m_mists(12.0f, C3Vector(44.0f, 44.0f, 25.0f), "textures\\Weather\\SnowMist01.blp", -1.5700001f, 0.34906587f, 9.0f, 3.0f, 128) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0078cd30 в IDA Pro / Ghidra
