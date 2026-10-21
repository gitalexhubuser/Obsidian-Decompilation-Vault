---
offset: "0x00509dd0"
module: "WoW/Source"
file: "WoW/Source/Ui/ChatFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00509dd0 — `CGChat_AddChatMessage`

- **Адрес (Offset):** `0x00509dd0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/ChatFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00509dd0
void CGChat::AddChatMessage(const char* text, int32_t type, const char* senderName, uint32_t language, const char* channelName, const char* targetName, const char* flags, WOWGUID senderGuid, uint32_t senderUnk, WOWGUID targetGuid, int32_t achievementID, bool isGM, const ChatConversation* conversation) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00509dd0 в IDA Pro / Ghidra
