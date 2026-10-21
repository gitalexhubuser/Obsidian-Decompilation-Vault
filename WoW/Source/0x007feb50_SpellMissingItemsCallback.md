---
offset: "0x007feb50"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007feb50 — `SpellMissingItemsCallback`

- **Адрес (Offset):** `0x007feb50`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007feb50
void SpellMissingItemsCallback(int32_t itemId, const WOWGUID& guid, void* param, bool success) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007feb50 в IDA Pro / Ghidra
