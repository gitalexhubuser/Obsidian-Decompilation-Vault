---
offset: "0x004fdbc0"
module: "WoW/Source"
file: "WoW/Source/Ui/ChatFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004fdbc0 — `SendChatEvent`

- **Адрес (Offset):** `0x004fdbc0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/ChatFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004fdbc0
static void SendChatEvent(ChatChannel* channel, uint32_t language, const char* text, int32_t type, const char* senderName, const char* channelString, const char* targetName, const char* flags, uint32_t lineID, WOWGUID guid, const ChatConversation* conversation) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004fdbc0 в IDA Pro / Ghidra
