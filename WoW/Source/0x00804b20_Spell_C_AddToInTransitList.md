---
offset: "0x00804b20"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00804b20 — `Spell_C_AddToInTransitList`

- **Адрес (Offset):** `0x00804b20`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00804b20
void Spell_C_AddToInTransitList(WOWGUID caster, const SpellRec* spell, uint32_t serverTime, uint32_t arrivalTime) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00804b20 в IDA Pro / Ghidra
