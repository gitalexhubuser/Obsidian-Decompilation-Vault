---
offset: "0x0078ca90"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Rain.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0078ca90 — `Rain_Rain`

- **Адрес (Offset):** `0x0078ca90`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Rain.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0078ca90
Rain::Rain(float width, float height) : m_bbox(C3Vector(0.0f, 0.0f, 0.0f), C3Vector(0.0f, 0.0f, 0.0f)), m_mists(12.0f, C3Vector(44.0f, 44.0f, 25.0f), "textures\\Weather\\SnowMist01.blp", -1.5700001f, 0.34906587f, 5.0f, 1.2f, 128) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0078ca90 в IDA Pro / Ghidra
