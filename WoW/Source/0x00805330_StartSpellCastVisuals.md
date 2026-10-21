---
offset: "0x00805330"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00805330 — `StartSpellCastVisuals`

- **Адрес (Offset):** `0x00805330`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00805330
void StartSpellCastVisuals(CGUnit_C* unit, PendingSpellCast* cast, const SpellRec* spell, int32_t castTime, bool hidden) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00805330 в IDA Pro / Ghidra
