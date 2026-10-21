---
offset: "0x007ece10"
module: "WoW/Source"
file: "WoW/Source/WorldClient/DayNight.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007ece10 — `DNClouds_Callback_GxTex`

- **Адрес (Offset):** `0x007ece10`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/DayNight.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007ece10
void DayNight::DNClouds::Callback_GxTex(EGxTexCommand command, uint32_t width, uint32_t height, uint32_t face, uint32_t level, void* userArg, uint32_t& texelStrideInBytes, const void*& texels) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007ece10 в IDA Pro / Ghidra
