---
offset: "0x00752710"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00752710 — `UnitCombatLogAuraAddedOrRemoved`

- **Адрес (Offset):** `0x00752710`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00752710
void UnitCombatLogAuraAddedOrRemoved(CGUnit_C* unit, AuraData* aura, const SpellRec* spell, uint8_t harmful, int32_t added) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00752710 в IDA Pro / Ghidra
