---
offset: "0x0074fe90"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0074fe90 — `CombatLogEntry_PendingCombatLogResolved`

- **Адрес (Offset):** `0x0074fe90`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0074fe90
void CombatLogEntry::PendingCombatLogResolved(int32_t id, const WOWGUID& guid, void* param, bool success) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0074fe90 в IDA Pro / Ghidra
