---
offset: "0x0058ba80"
module: "WoW/Source"
file: "WoW/Source/Ui/QuestFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0058ba80 — `CGQuestInfo_AddItemRequest`

- **Адрес (Offset):** `0x0058ba80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/QuestFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0058ba80
void CGQuestInfo::AddItemRequest(const char* title, const uint32_t* itemIds, const uint32_t* itemCounts, const uint32_t* itemDisplays, int32_t numItems, int32_t requiredMoney, int32_t canComplete, int32_t autoLaunched, int32_t suggestedGroupNum, uint32_t questFlags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0058ba80 в IDA Pro / Ghidra
