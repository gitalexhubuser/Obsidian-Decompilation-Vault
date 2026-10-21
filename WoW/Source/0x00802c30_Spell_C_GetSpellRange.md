---
offset: "0x00802c30"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00802c30 — `Spell_C_GetSpellRange`

- **Адрес (Offset):** `0x00802c30`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00802c30
void Spell_C::GetSpellRange(CGUnit_C* caster, int32_t spellId, float* minRange, float* maxRange, CGObject_C* target) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00802c30 в IDA Pro / Ghidra
