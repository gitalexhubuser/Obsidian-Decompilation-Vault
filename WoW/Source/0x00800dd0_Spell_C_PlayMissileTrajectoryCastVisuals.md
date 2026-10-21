---
offset: "0x00800dd0"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00800dd0 — `Spell_C_PlayMissileTrajectoryCastVisuals`

- **Адрес (Offset):** `0x00800dd0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00800dd0
void Spell_C_PlayMissileTrajectoryCastVisuals(CGUnit_C* unit, PendingSpellCast* cast, const SpellRec* spell, const SpellVisualRec* visual, const SpellVisualKitRec* kit, const TSStackArray<CGUnit_C*>* targets, float time) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00800dd0 в IDA Pro / Ghidra
