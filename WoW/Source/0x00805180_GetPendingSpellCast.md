---
offset: "0x00805180"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00805180 — `GetPendingSpellCast`

- **Адрес (Offset):** `0x00805180`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00805180
PendingSpellCast* GetPendingSpellCast(uint8_t castCount, int32_t spellId, const WOWGUID& caster) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00805180 в IDA Pro / Ghidra
