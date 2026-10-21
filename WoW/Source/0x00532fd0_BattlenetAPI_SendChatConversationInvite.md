---
offset: "0x00532fd0"
module: "WoW/Source"
file: "WoW/Source/Ui/BattlenetAPI.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00532fd0 — `BattlenetAPI_SendChatConversationInvite`

- **Адрес (Offset):** `0x00532fd0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/BattlenetAPI.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00532fd0
uint16_t BattlenetAPI::SendChatConversationInvite(uint8_t channel, const Battlenet::Toon::FullName* toon, GeneralFunction::Callback* callback) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00532fd0 в IDA Pro / Ghidra
