---
offset: "0x0057aaf0"
module: "WoW/Source"
file: "WoW/Source/Ui/QuestTextParser.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0057aaf0 — `SpellParserParseSubText`

- **Адрес (Offset):** `0x0057aaf0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/QuestTextParser.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0057aaf0
static int32_t SpellParserParseSubText(const SpellRec* spell, char* buffer, uint32_t size, int32_t parsePet, int32_t parseUnit, int32_t spellLevel, int32_t scale, int32_t noModifiers, const char* text, const char** cursor) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0057aaf0 в IDA Pro / Ghidra
