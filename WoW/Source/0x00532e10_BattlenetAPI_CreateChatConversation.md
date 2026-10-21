---
offset: "0x00532e10"
module: "WoW/Source"
file: "WoW/Source/Ui/BattlenetAPI.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00532e10 — `BattlenetAPI_CreateChatConversation`

- **Адрес (Offset):** `0x00532e10`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/BattlenetAPI.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00532e10
uint16_t BattlenetAPI::CreateChatConversation(const Battlenet::Toon::FullName* first, const Battlenet::Toon::FullName* second, GeneralFunction::Callback* callback) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00532e10 в IDA Pro / Ghidra
