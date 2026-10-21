---
offset: "0x00807980"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00807980 — `SpellHistory_GetSpellCooldown`

- **Адрес (Offset):** `0x00807980`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00807980
bool SpellHistory::GetSpellCooldown(int32_t spellId, int32_t itemId, uint32_t* duration, uint32_t* start, uint32_t* enable) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00807980 в IDA Pro / Ghidra
