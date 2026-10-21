---
offset: "0x006b94c0"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/AccountData.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b94c0 — `Packet_SMSG_ACCOUNT_DATA_TIMES`

- **Адрес (Offset):** `0x006b94c0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/AccountData.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b94c0
static int32_t Packet_SMSG_ACCOUNT_DATA_TIMES(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b94c0 в IDA Pro / Ghidra
