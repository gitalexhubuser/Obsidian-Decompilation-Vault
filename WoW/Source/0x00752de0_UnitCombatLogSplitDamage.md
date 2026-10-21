---
offset: "0x00752de0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00752de0 — `UnitCombatLogSplitDamage`

- **Адрес (Offset):** `0x00752de0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00752de0
void UnitCombatLogSplitDamage(const WOWGUID& source, const WOWGUID& dest, int32_t spellId, int32_t damage, int32_t overkill, uint32_t school, int32_t absorbed, int32_t resisted, int32_t blocked, uint32_t hitInfo, uint32_t timeOffset) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00752de0 в IDA Pro / Ghidra
