---
offset: "0x0074e1a0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0074e1a0 — `CombatLogFilter_MatchesFilter`

- **Адрес (Offset):** `0x0074e1a0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0074e1a0
bool CombatLogFilter::MatchesFilter(int32_t event, const WOWGUID& sourceGuid, uint32_t sourceFlags, const WOWGUID& destGuid, uint32_t destFlags, int32_t spellId, const char* spellName) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0074e1a0 в IDA Pro / Ghidra
