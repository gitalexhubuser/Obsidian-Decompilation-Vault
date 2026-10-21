---
offset: "0x00750860"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00750860 — `SendHealEvent`

- **Адрес (Offset):** `0x00750860`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00750860
void SendHealEvent(int32_t event, const WOWGUID& source, const WOWGUID& dest, const SpellRec* spell, int32_t amount, int32_t overheal, int32_t absorbed, bool crit, uint32_t timeOffset) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00750860 в IDA Pro / Ghidra
