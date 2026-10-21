---
offset: "0x00750660"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00750660 — `SendDamageEvent`

- **Адрес (Offset):** `0x00750660`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00750660
void SendDamageEvent(int32_t event, const WOWGUID& source, const WOWGUID& dest, const SpellRec* spell, int32_t damage, int32_t overkill, uint32_t school, int32_t resisted, int32_t blocked, int32_t absorbed, bool crit, bool a11, bool a12, uint32_t timeOffset) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00750660 в IDA Pro / Ghidra
