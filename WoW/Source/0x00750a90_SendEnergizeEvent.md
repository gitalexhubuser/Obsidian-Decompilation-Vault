---
offset: "0x00750a90"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00750a90 — `SendEnergizeEvent`

- **Адрес (Offset):** `0x00750a90`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00750a90
void SendEnergizeEvent(int32_t event, const WOWGUID& source, const WOWGUID& dest, const SpellRec* spell, int32_t powerType, int32_t amount, uint32_t timeOffset) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00750a90 в IDA Pro / Ghidra
