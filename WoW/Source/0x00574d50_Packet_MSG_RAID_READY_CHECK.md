---
offset: "0x00574d50"
module: "WoW/Source"
file: "WoW/Source/Ui/RaidInfo.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00574d50 — `Packet_MSG_RAID_READY_CHECK`

- **Адрес (Offset):** `0x00574d50`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/RaidInfo.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00574d50
int32_t Packet_MSG_RAID_READY_CHECK(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00574d50 в IDA Pro / Ghidra
