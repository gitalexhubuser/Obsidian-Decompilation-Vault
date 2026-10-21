---
offset: "0x00809f80"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00809f80 — `Spell_C_PrepareMissileTrajectoryCast`

- **Адрес (Offset):** `0x00809f80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00809f80
int32_t Spell_C_PrepareMissileTrajectoryCast(CGUnit_C* caster, PendingSpellCast* cast, const SpellRec* spell, const TSStackArray<CGUnit_C*>* targets, float* pitch, float* speed) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00809f80 в IDA Pro / Ghidra
