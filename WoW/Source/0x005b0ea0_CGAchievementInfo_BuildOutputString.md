---
offset: "0x005b0ea0"
module: "WoW/Source"
file: "WoW/Source/Ui/AchievementInfo.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x005b0ea0 — `CGAchievementInfo_BuildOutputString`

- **Адрес (Offset):** `0x005b0ea0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/AchievementInfo.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x005b0ea0
uint64_t CGAchievementInfo::BuildOutputString(char* buffer, int32_t size, uint64_t sum, uint64_t highest, int32_t highestId, uint64_t count, uint64_t value, CLIENT_ACHIEVEMENT_CRITERIA* criteria, int32_t flags, int32_t criteriaFlags, bool completed, const AchievementRec* achievement, const Achievement_CriteriaRec* criteriaRec, int32_t required) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x005b0ea0 в IDA Pro / Ghidra
