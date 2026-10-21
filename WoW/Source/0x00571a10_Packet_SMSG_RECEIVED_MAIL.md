---
offset: "0x00571a10"
module: "WoW/Source"
file: "WoW/Source/Ui/MailInfo.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00571a10 — `Packet_SMSG_RECEIVED_MAIL`

- **Адрес (Offset):** `0x00571a10`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/MailInfo.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00571a10
int32_t Packet_SMSG_RECEIVED_MAIL(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00571a10 в IDA Pro / Ghidra
