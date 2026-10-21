---
offset: "0x00502ea0"
module: "WoW/Source"
file: "WoW/Source/Ui/ChatFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00502ea0 — `CGChat_QueueTextEmote`

- **Адрес (Offset):** `0x00502ea0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/ChatFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00502ea0
void CGChat::QueueTextEmote(const WOWGUID& guid, uint32_t emote, const char* target, int32_t queued, uint32_t emoteNum) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00502ea0 в IDA Pro / Ghidra
