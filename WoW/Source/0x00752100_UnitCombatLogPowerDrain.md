---
offset: "0x00752100"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00752100 — `UnitCombatLogPowerDrain`

- **Адрес (Offset):** `0x00752100`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00752100
void UnitCombatLogPowerDrain(const WOWGUID& casterGuid, const WOWGUID& targetGuid, int32_t spellId, uint32_t powerType, uint32_t amount, float multiplier, bool a7, uint32_t timeOffset) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00752100 в IDA Pro / Ghidra
