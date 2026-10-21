---
offset: "0x00808200"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00808200 — `Spell_C_SpellFailed`

- **Адрес (Offset):** `0x00808200`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00808200
void Spell_C_SpellFailed(PendingSpellCast* cast, const SpellRec* spell, int32_t reason, int32_t misc1, int32_t misc2, bool resetCooldown) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00808200 в IDA Pro / Ghidra
