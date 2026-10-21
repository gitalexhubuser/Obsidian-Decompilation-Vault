---
offset: "0x0058ba00"
module: "WoW/Source"
file: "WoW/Source/Ui/QuestFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0058ba00 — `CGQuestInfo_AddQuestInProgress`

- **Адрес (Offset):** `0x0058ba00`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/QuestFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0058ba00
void CGQuestInfo::AddQuestInProgress(int32_t questId, const char* title, int32_t level, int32_t flags, int32_t repeatable) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0058ba00 в IDA Pro / Ghidra
