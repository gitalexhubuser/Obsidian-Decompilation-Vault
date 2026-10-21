---
offset: "0x00502d00"
module: "WoW/Source"
file: "WoW/Source/Ui/ChatFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00502d00 — `CGChat_QueueChatText`

- **Адрес (Offset):** `0x00502d00`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/ChatFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00502d00
void CGChat::QueueChatText(const char* text, int32_t type, const char* senderName, const char* targetName, uint32_t language, const char* channelName, const char* flags, int32_t queued, int32_t a9, WOWGUID senderGuid, uint32_t senderUnk, WOWGUID targetGuid, int32_t achievementID, bool isGM, const ChatConversation* conversation) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00502d00 в IDA Pro / Ghidra
