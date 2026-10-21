---
offset: "0x007ffb60"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007ffb60 — `CheckItemRequirement`

- **Адрес (Offset):** `0x007ffb60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007ffb60
static bool CheckItemRequirement(const PendingSpellCast* cast, const SpellRec* spell, WOWGUID itemGuid, int32_t* reason) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007ffb60 в IDA Pro / Ghidra
