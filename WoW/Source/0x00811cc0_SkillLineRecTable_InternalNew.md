---
offset: "0x00811cc0"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/SpellTable.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00811cc0 — `SkillLineRecTable_InternalNew`

- **Адрес (Offset):** `0x00811cc0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/SpellTable.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00811cc0
SKILLLINEREC* SkillLineRecTable::InternalNew(TSExplicitList<SKILLLINEREC>* listptr, size_t extrabytes, uint32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00811cc0 в IDA Pro / Ghidra
