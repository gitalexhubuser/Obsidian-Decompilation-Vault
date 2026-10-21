---
offset: "0x005bfab0"
module: "WoW/Source"
file: "WoW/Source/Ui/Calendar.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x005bfab0 — `ComputeEventOccurrence`

- **Адрес (Offset):** `0x005bfab0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/Calendar.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x005bfab0
static bool ComputeEventOccurrence(const WowTime* now, const WowTime* rangeStart, const WowTime* rangeEnd, WowTime* outEnd, HolidaysRec* holiday, int32_t index, bool* weekly, int32_t interval, WowTime* outStart) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x005bfab0 в IDA Pro / Ghidra
