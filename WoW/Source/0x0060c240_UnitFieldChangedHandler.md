---
offset: "0x0060c240"
module: "WoW/Source"
file: "WoW/Source/Ui/ScriptEvents.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0060c240 — `UnitFieldChangedHandler`

- **Адрес (Offset):** `0x0060c240`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/ScriptEvents.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0060c240
static int32_t UnitFieldChangedHandler(WOWGUID guid, uint32_t fieldOffset, uint32_t fieldSize, const void* oldValue, void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0060c240 в IDA Pro / Ghidra
