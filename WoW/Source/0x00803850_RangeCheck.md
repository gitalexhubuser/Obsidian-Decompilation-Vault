---
offset: "0x00803850"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00803850 — `RangeCheck`

- **Адрес (Offset):** `0x00803850`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00803850
static bool RangeCheck(CGUnit_C* caster, int32_t spellId, CGObject_C* target, uint8_t* tooFar) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00803850 в IDA Pro / Ghidra
