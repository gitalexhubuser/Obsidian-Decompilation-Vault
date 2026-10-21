---
offset: "0x005e1ff0"
module: "WoW/Source"
file: "WoW/Source/Ui/QuestLog.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x005e1ff0 — `CountQuestItemDropsNeeded`

- **Адрес (Offset):** `0x005e1ff0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/QuestLog.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x005e1ff0
int32_t CountQuestItemDropsNeeded(int32_t questId, void (*callback)(int32_t id, const WOWGUID& guid, void* param, bool success), void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x005e1ff0 в IDA Pro / Ghidra
