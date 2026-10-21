---
offset: "0x0060abf0"
module: "WoW/Source"
file: "WoW/Source/Ui/ScriptEvents.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0060abf0 — `Script_GetGUIDFromToken`

- **Адрес (Offset):** `0x0060abf0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/ScriptEvents.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0060abf0
bool Script_GetGUIDFromToken(const char* token, WOWGUID& guid, bool defaultToTarget) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0060abf0 в IDA Pro / Ghidra
