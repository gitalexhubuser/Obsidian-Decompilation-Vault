---
offset: "0x006b3280"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/FriendList.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b3280 — `Packet_SMSG_WHOIS`

- **Адрес (Offset):** `0x006b3280`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/FriendList.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b3280
int32_t Packet_SMSG_WHOIS(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b3280 в IDA Pro / Ghidra
