---
offset: "0x006b8700"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/FriendList.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b8700 — `Packet_SMSG_CONTACT_LIST`

- **Адрес (Offset):** `0x006b8700`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/FriendList.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b8700
int32_t Packet_SMSG_CONTACT_LIST(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b8700 в IDA Pro / Ghidra
