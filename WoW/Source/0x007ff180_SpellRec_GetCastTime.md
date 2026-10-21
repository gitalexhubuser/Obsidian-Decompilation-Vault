---
offset: "0x007ff180"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007ff180 — `SpellRec_GetCastTime`

- **Адрес (Offset):** `0x007ff180`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007ff180
int32_t SpellRec::GetCastTime(const SpellRec* spell, int32_t isPet, int32_t isUnit, int32_t allowNegative) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007ff180 в IDA Pro / Ghidra
