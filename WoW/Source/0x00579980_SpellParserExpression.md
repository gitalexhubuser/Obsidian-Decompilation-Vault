---
offset: "0x00579980"
module: "WoW/Source"
file: "WoW/Source/Ui/QuestTextParser.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00579980 — `SpellParserExpression`

- **Адрес (Offset):** `0x00579980`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/QuestTextParser.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00579980
static int32_t SpellParserExpression(const SpellRec* spell, char* buffer, uint32_t size, int32_t parsePet, int32_t parseUnit, int32_t spellLevel, int32_t scale, int32_t noModifiers, int32_t* intValue, float* value, const char** cursor, const char* end) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00579980 в IDA Pro / Ghidra
