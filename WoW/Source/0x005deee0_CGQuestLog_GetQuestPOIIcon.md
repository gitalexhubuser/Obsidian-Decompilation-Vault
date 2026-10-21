---
offset: "0x005deee0"
module: "WoW/Source"
file: "WoW/Source/Ui/QuestLog.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x005deee0 — `CGQuestLog_GetQuestPOIIcon`

- **Адрес (Offset):** `0x005deee0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/QuestLog.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x005deee0
bool CGQuestLog::GetQuestPOIIcon(int32_t questId, bool* complete, int32_t* mapId, uint32_t* mapFloor, int32_t* x, int32_t* y, int32_t* objective) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x005deee0 в IDA Pro / Ghidra
