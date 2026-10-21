---
offset: "0x00403de0"
module: "WoW/Source"
file: "WoW/Source/Client.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00403de0 — `Packet_SMSG_LOGIN_VERIFY_WORLD`

- **Адрес (Offset):** `0x00403de0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Client.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00403de0
static int32_t Packet_SMSG_LOGIN_VERIFY_WORLD(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00403de0 в IDA Pro / Ghidra
