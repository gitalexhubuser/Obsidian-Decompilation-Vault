---
offset: "0x007f0d40"
module: "WoW/Source"
file: "WoW/Source/WorldClient/DayNight.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007f0d40 — `LightQueue_LightQueue`

- **Адрес (Offset):** `0x007f0d40`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/DayNight.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007f0d40
DayNight::LightQueue::LightQueue(const uint32_t* params) : CMemBlock(sizeof(LightQE) * params[0], 0, typeid(LightQE).raw_name(), SLOG_OBJECT) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007f0d40 в IDA Pro / Ghidra
