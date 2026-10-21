---
offset: "0x0074e050"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0074e050 — `CombatLogFilter_SetFilterData`

- **Адрес (Offset):** `0x0074e050`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0074e050
bool CombatLogFilter::SetFilterData(const char* events, const WOWGUID& sourceGuid, uint32_t sourceFlags, const WOWGUID& destGuid, uint32_t destFlags, int32_t spellId, const char* spellName) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0074e050 в IDA Pro / Ghidra
