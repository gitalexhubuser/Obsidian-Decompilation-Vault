---
offset: "0x00752520"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00752520 — `CombatLog_AddSpellDamageEntry`

- **Адрес (Offset):** `0x00752520`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00752520
void CombatLog::AddSpellDamageEntry(const WOWGUID& source, const WOWGUID& dest, int32_t spellId, int32_t damage, uint32_t timeOffset) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00752520 в IDA Pro / Ghidra
