---
offset: "0x00751f70"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00751f70 — `UnitCombatLogHeal`

- **Адрес (Offset):** `0x00751f70`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00751f70
void UnitCombatLogHeal(const WOWGUID& casterGuid, const WOWGUID& targetGuid, int32_t spellId, int32_t amount, int32_t overheal, int32_t absorbed, bool crit, bool periodic, uint32_t timeOffset) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00751f70 в IDA Pro / Ghidra
