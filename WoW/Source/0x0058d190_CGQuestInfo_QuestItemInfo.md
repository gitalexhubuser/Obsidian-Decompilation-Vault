---
offset: "0x0058d190"
module: "WoW/Source"
file: "WoW/Source/Ui/QuestFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0058d190 — `CGQuestInfo_QuestItemInfo`

- **Адрес (Offset):** `0x0058d190`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/QuestFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0058d190
int32_t CGQuestInfo::QuestItemInfo(const char* type, uint32_t index, char* name, uint32_t nameSize, char* texture, uint32_t textureSize, int32_t* count, int32_t* quality, int32_t* usable) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0058d190 в IDA Pro / Ghidra
