---
offset: "0x00578f20"
module: "WoW/Source"
file: "WoW/Source/Ui/QuestTextParser.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00578f20 — `QuestParserParseToken`

- **Адрес (Offset):** `0x00578f20`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/QuestTextParser.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00578f20
bool QuestParserParseToken(char* buffer, uint32_t size, const NameCache* record, const char* name, int32_t achievement, WOWGUID guid, const CGUnit_C* unit, const char** cursor) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00578f20 в IDA Pro / Ghidra
