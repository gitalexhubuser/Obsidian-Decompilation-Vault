---
offset: "0x00806200"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00806200 — `Spell_C_CancelSpell`

- **Адрес (Offset):** `0x00806200`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00806200
void Spell_C_CancelSpell(PendingSpellCast* cast, bool stopRecast, bool notifyServer, int32_t reason) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00806200 в IDA Pro / Ghidra
