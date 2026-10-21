---
offset: "0x007ff770"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007ff770 — `Spell_C_GetMinMaxPoints`

- **Адрес (Offset):** `0x007ff770`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007ff770
void Spell_C_GetMinMaxPoints(const SpellRec* spell, uint32_t effectIndex, float* minPoints, float* maxPoints, int32_t spellLevel, int32_t isPet, int32_t isUnit, int32_t noModifiers) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007ff770 в IDA Pro / Ghidra
