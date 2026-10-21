---
offset: "0x0060bf60"
module: "WoW/Source"
file: "WoW/Source/Ui/ScriptEvents.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0060bf60 — `Script_SendUnitSpellSignal`

- **Адрес (Offset):** `0x0060bf60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/ScriptEvents.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0060bf60
void Script_SendUnitSpellSignal(const WOWGUID& guid, uint8_t castCount, const SpellRec* spell, int32_t signal) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0060bf60 в IDA Pro / Ghidra
