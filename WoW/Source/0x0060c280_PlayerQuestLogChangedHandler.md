---
offset: "0x0060c280"
module: "WoW/Source"
file: "WoW/Source/Ui/ScriptEvents.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0060c280 — `PlayerQuestLogChangedHandler`

- **Адрес (Offset):** `0x0060c280`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/ScriptEvents.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0060c280
static int32_t PlayerQuestLogChangedHandler(WOWGUID guid, uint32_t fieldOffset, uint32_t fieldSize, const void* oldValue, void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0060c280 в IDA Pro / Ghidra
