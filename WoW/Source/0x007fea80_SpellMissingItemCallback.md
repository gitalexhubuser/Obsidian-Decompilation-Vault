---
offset: "0x007fea80"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/Spell_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007fea80 — `SpellMissingItemCallback`

- **Адрес (Offset):** `0x007fea80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/Spell_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007fea80
void SpellMissingItemCallback(int32_t itemId, const WOWGUID& guid, void* param, bool success) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007fea80 в IDA Pro / Ghidra
