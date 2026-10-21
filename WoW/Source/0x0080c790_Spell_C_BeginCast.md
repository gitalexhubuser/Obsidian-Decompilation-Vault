---
offset: "0x0080c790"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0080c790 — `Spell_C_BeginCast`

- **Адрес (Offset):** `0x0080c790`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0080c790
static bool Spell_C_BeginCast(CGUnit_C* caster, const SpellRec* spell, WOWGUID target, PendingSpellCast* cast, bool confirmed) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0080c790 в IDA Pro / Ghidra
