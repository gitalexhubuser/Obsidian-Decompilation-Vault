---
offset: "0x00401480"
module: "WoW/Source"
file: "WoW/Source/Client.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00401480 — `Packet_SMSG_TRANSFER_PENDING`

- **Адрес (Offset):** `0x00401480`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Client.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00401480
int32_t Packet_SMSG_TRANSFER_PENDING(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00401480 в IDA Pro / Ghidra
