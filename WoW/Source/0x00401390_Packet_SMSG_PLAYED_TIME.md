---
offset: "0x00401390"
module: "WoW/Source"
file: "WoW/Source/Client.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00401390 — `Packet_SMSG_PLAYED_TIME`

- **Адрес (Offset):** `0x00401390`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Client.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00401390
int32_t Packet_SMSG_PLAYED_TIME(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00401390 в IDA Pro / Ghidra
