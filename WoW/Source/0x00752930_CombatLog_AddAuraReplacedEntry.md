---
offset: "0x00752930"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00752930 — `CombatLog_AddAuraReplacedEntry`

- **Адрес (Offset):** `0x00752930`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00752930
void CombatLog::AddAuraReplacedEntry(const WOWGUID& source, const WOWGUID& dest, int32_t spellId, int32_t replacedSpellId, uint8_t harmful, bool stolen, uint32_t timeOffset) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00752930 в IDA Pro / Ghidra
