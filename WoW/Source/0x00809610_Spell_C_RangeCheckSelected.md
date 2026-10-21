---
offset: "0x00809610"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00809610 — `Spell_C_RangeCheckSelected`

- **Адрес (Offset):** `0x00809610`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00809610
bool Spell_C_RangeCheckSelected(CGUnit_C* caster, const SpellRec* spell, WOWGUID target, uint8_t* inRange, bool report, PendingSpellCast* cast) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00809610 в IDA Pro / Ghidra
