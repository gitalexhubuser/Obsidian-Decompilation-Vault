---
offset: "0x008051d0"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008051d0 — `FindPendingSpellCast`

- **Адрес (Offset):** `0x008051d0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008051d0
PendingSpellCast* FindPendingSpellCast(const WOWGUID& castItem, PendingSpellCast* fallback, uint8_t castCount, int32_t spellId, const WOWGUID& caster) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008051d0 в IDA Pro / Ghidra
