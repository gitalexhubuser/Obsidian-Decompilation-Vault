---
offset: "0x00752a40"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00752a40 — `CombatLog_AddSpellRemoveEntry`

- **Адрес (Offset):** `0x00752a40`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00752a40
void CombatLog::AddSpellRemoveEntry(const WOWGUID& source, const WOWGUID& dest, int32_t dispelSpellId, int32_t spellId, uint8_t harmful) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00752a40 в IDA Pro / Ghidra
