---
offset: "0x00512850"
module: "WoW/Source"
file: "WoW/Source/Ui/GameUI_CVar.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00512850 — `CVarHandler_autoCompleteWhenEditingFromCenter`

- **Адрес (Offset):** `0x00512850`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/GameUI_CVar.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00512850
bool CVarHandler_autoCompleteWhenEditingFromCenter(CVar* var, const char* oldValue, const char* value, void* arg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00512850 в IDA Pro / Ghidra
