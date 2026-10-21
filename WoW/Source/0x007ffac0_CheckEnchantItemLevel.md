---
offset: "0x007ffac0"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007ffac0 — `CheckEnchantItemLevel`

- **Адрес (Offset):** `0x007ffac0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007ffac0
static bool CheckEnchantItemLevel(const PendingSpellCast* cast, const SpellRec* spell, const ItemStats_C* stats, const CGItem_C* item, int32_t* reason) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007ffac0 в IDA Pro / Ghidra
