---
offset: "0x00805f60"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00805f60 — `Spell_C_IsSpellPending`

- **Адрес (Offset):** `0x00805f60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00805f60
static bool Spell_C_IsSpellPending(const WOWGUID& castItem, int32_t spellId, const PendingSpellCast* except) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00805f60 в IDA Pro / Ghidra
