---
offset: "0x007ff480"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007ff480 — `Spell_C_GetMinMaxRange`

- **Адрес (Offset):** `0x007ff480`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007ff480
void Spell_C_GetMinMaxRange(CGUnit_C* caster, const SpellRec* spell, float* minRange, float* maxRange, int32_t friendly, CGObject_C* target) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007ff480 в IDA Pro / Ghidra
