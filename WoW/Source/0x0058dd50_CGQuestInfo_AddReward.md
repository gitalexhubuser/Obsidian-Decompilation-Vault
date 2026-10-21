---
offset: "0x0058dd50"
module: "WoW/Source"
file: "WoW/Source/Ui/QuestFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0058dd50 — `CGQuestInfo_AddReward`

- **Адрес (Offset):** `0x0058dd50`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/QuestFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0058dd50
void CGQuestInfo::AddReward(const char* title, const uint32_t* choiceItems, const uint32_t* choiceDisplays, const uint32_t* choiceCounts, int32_t numChoices, const uint32_t* rewardItems, const uint32_t* rewardDisplays, const uint32_t* rewardCounts, int32_t numRewards, int32_t money, int32_t xp, uint32_t honor, float honorMultiplier, int32_t spell, int32_t spellCast, int32_t autoLaunched, int32_t suggestedGroupNum, int32_t rewardTitle, int32_t talents, int32_t arenaPoints, uint32_t factionMask, const uint32_t* factionIDs, const uint32_t* factionValues, const uint32_t* factionOverrides, uint32_t questFlags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0058dd50 в IDA Pro / Ghidra
