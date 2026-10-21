---
offset: "0x007e28e0"
module: "WoW/Source"
file: "WoW/Source/Game/ClientGameTime.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007e28e0 — `Packet_SMSG_LOGIN_SETTIMESPEED`

- **Адрес (Offset):** `0x007e28e0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Game/ClientGameTime.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007e28e0
static int32_t Packet_SMSG_LOGIN_SETTIMESPEED(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007e28e0 в IDA Pro / Ghidra
