---
offset: "0x00540670"
module: "WoW/Source"
file: "WoW/Source/Ui/SpellBookFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00540670 — `GetSlotFromLua`

- **Адрес (Offset):** `0x00540670`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/SpellBookFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00540670
bool GetSlotFromLua(lua_State* L, uint32_t* slot, int32_t* petSpell, int32_t* type, int32_t allowName) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00540670 в IDA Pro / Ghidra
