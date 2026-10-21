---
offset: "0x00750500"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00750500 — `CombatLog_QueueMissedSpellText`

- **Адрес (Offset):** `0x00750500`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00750500
void CombatLog::QueueMissedSpellText(const WOWGUID& source, const WOWGUID& dest, int32_t event, const SpellRec* spell, int32_t missType, int32_t amount, uint32_t timeOffset) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00750500 в IDA Pro / Ghidra
