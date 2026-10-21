---
offset: "0x00804430"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00804430 — `Spell_C_CancelsAuraEffect`

- **Адрес (Offset):** `0x00804430`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00804430
bool Spell_C_CancelsAuraEffect(const CGUnit_C* unit, const SpellRec* spell, int32_t auraType, int32_t* reason) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00804430 в IDA Pro / Ghidra
