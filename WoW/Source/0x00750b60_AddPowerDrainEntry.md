---
offset: "0x00750b60"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00750b60 — `AddPowerDrainEntry`

- **Адрес (Offset):** `0x00750b60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00750b60
void AddPowerDrainEntry(int32_t event, const WOWGUID& source, const WOWGUID& dest, const SpellRec* spell, int32_t amount, int32_t powerType, int32_t extra, uint32_t timeOffset) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00750b60 в IDA Pro / Ghidra
