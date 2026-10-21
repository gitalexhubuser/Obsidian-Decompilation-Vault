---
offset: "0x0074f350"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0074f350 — `GetPendingCombatLogData`

- **Адрес (Offset):** `0x0074f350`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0074f350
PendingCombatLogData* GetPendingCombatLogData(CombatLogEntry* entry, const WOWGUID& guid, uint32_t mask) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0074f350 в IDA Pro / Ghidra
