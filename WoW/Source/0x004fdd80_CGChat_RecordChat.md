---
offset: "0x004fdd80"
module: "WoW/Source"
file: "WoW/Source/Ui/ChatFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004fdd80 — `CGChat_RecordChat`

- **Адрес (Offset):** `0x004fdd80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/ChatFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004fdd80
void CGChat::RecordChat(const char* text, int32_t type, const char* senderName, WOWGUID senderGuid, uint32_t senderUnk, uint32_t a6, const char* channelName, uint32_t lineID, const CGPlayer_C* player) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004fdd80 в IDA Pro / Ghidra
