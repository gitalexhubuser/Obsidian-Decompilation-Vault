---
offset: "0x00752040"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00752040 — `UnitCombatLogEnergize`

- **Адрес (Offset):** `0x00752040`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00752040
void UnitCombatLogEnergize(const WOWGUID& casterGuid, const WOWGUID& targetGuid, int32_t spellId, int32_t powerType, int32_t amount, bool periodic, uint32_t timeOffset) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00752040 в IDA Pro / Ghidra
