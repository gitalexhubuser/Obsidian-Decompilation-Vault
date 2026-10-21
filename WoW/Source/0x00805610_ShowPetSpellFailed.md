---
offset: "0x00805610"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00805610 — `ShowPetSpellFailed`

- **Адрес (Offset):** `0x00805610`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00805610
void ShowPetSpellFailed(PendingSpellCast* cast, const SpellRec* spell, int32_t reason, int32_t misc1, int32_t misc2) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00805610 в IDA Pro / Ghidra
