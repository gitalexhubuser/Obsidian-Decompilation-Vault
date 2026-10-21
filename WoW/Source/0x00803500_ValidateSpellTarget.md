---
offset: "0x00803500"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00803500 — `ValidateSpellTarget`

- **Адрес (Offset):** `0x00803500`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00803500
static bool ValidateSpellTarget(CGUnit_C* caster, const SpellRec* spell, uint32_t count, CGUnit_C** targets, int32_t* reason, bool casterIncluded) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00803500 в IDA Pro / Ghidra
