---
offset: "0x00520190"
module: "WoW/Source"
file: "WoW/Source/Ui/GameUI.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00520190 — `CGGameUI_ClosestObjectMatch`

- **Адрес (Offset):** `0x00520190`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/GameUI.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00520190
WOWGUID CGGameUI::ClosestObjectMatch(const char* name, uint32_t typeMask, int32_t targetType, int32_t exact, float maxDistance, int32_t ignoreHostileTotems) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00520190 в IDA Pro / Ghidra
