---
offset: "0x0080b5d0"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0080b5d0 — `Spell_C_IsUsableAction`

- **Адрес (Offset):** `0x0080b5d0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0080b5d0
bool Spell_C_IsUsableAction(CGUnit_C* unit, const SpellRec* spell, const WOWGUID& target, const ItemStats_C* item, bool ignoreControl) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0080b5d0 в IDA Pro / Ghidra
