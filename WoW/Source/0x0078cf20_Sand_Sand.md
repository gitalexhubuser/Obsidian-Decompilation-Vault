---
offset: "0x0078cf20"
module: "WoW/Source"
file: "WoW/Source/WorldClient/Sand.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0078cf20 — `Sand_Sand`

- **Адрес (Offset):** `0x0078cf20`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/Sand.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0078cf20
Sand::Sand(float width, float height) : m_bbox(C3Vector(0.0f, 0.0f, 0.0f), C3Vector(0.0f, 0.0f, 0.0f)), m_mists(12.0f, C3Vector(44.0f, 44.0f, 25.0f), "textures\\Weather\\WeatherMistGrainy01.blp", -1.5700001f, 0.34906587f, 15.0f, 4.5f, 128) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0078cf20 в IDA Pro / Ghidra
