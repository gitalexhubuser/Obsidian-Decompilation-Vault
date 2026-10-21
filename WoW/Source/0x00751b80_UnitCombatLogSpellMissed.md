---
offset: "0x00751b80"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00751b80 — `UnitCombatLogSpellMissed`

- **Адрес (Offset):** `0x00751b80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/UnitCombatLog_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00751b80
void UnitCombatLogSpellMissed(const WOWGUID& casterGuid, const WOWGUID& targetGuid, int32_t spellId, int32_t missType, bool a5, bool a6, int32_t a7) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00751b80 в IDA Pro / Ghidra
