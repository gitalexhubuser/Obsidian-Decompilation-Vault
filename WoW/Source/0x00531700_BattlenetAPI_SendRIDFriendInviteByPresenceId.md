---
offset: "0x00531700"
module: "WoW/Source"
file: "WoW/Source/Ui/BattlenetAPI.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00531700 — `BattlenetAPI_SendRIDFriendInviteByPresenceId`

- **Адрес (Offset):** `0x00531700`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/BattlenetAPI.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00531700
uint16_t BattlenetAPI::SendRIDFriendInviteByPresenceId(uint32_t presenceId, const char* note, GeneralFunction::Callback* callback) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00531700 в IDA Pro / Ghidra
