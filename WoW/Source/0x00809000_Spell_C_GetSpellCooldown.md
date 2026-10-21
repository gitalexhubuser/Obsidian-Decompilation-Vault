---
offset: "0x00809000"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00809000 — `Spell_C_GetSpellCooldown`

- **Адрес (Offset):** `0x00809000`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00809000
bool Spell_C_GetSpellCooldown(int32_t spellId, int32_t petSpell, uint32_t* duration, uint32_t* start, uint32_t* enable) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00809000 в IDA Pro / Ghidra
