---
offset: "0x0080cce0"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0080cce0 — `Spell_C_CastSpell`

- **Адрес (Offset):** `0x0080cce0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0080cce0
bool Spell_C_CastSpell(CGUnit_C* caster, int32_t spellId, const CGItem_C* item, WOWGUID target, PendingSpellCast* cast, bool confirmed) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0080cce0 в IDA Pro / Ghidra
