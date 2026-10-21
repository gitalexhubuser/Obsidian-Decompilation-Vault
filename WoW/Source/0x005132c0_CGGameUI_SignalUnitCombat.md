---
offset: "0x005132c0"
module: "WoW/Source"
file: "WoW/Source/Ui/GameUI.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x005132c0 — `CGGameUI_SignalUnitCombat`

- **Адрес (Offset):** `0x005132c0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/GameUI.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x005132c0
void CGGameUI::SignalUnitCombat(const WOWGUID& guid, const char* action, int32_t amount, uint32_t schoolMask, uint32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x005132c0 в IDA Pro / Ghidra
