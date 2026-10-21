---
offset: "0x00800120"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00800120 — `CreateMissilesForTargetPoints`

- **Адрес (Offset):** `0x00800120`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00800120
void CreateMissilesForTargetPoints(const TSStackArray<SpellCastTargetPoint>& points, CGUnit_C* unit, const SpellRec* spell, const SpellVisualRec* visual, uint32_t ammoDisplayId, uint32_t ammoInventoryType, PendingSpellCastData* data, uint32_t delay) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00800120 в IDA Pro / Ghidra
