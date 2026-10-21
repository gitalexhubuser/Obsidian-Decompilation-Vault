---
offset: "0x0058c5a0"
module: "WoW/Source"
file: "WoW/Source/Ui/QuestFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0058c5a0 — `CGQuestInfo_SetState`

- **Адрес (Offset):** `0x0058c5a0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/QuestFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0058c5a0
void CGQuestInfo::SetState(WOWGUID npc, WOWGUID inform, int32_t state, const char* text, int32_t questId, int32_t startCheat) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0058c5a0 в IDA Pro / Ghidra
