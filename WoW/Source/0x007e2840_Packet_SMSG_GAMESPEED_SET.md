---
offset: "0x007e2840"
module: "WoW/Source"
file: "WoW/Source/Game/ClientGameTime.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007e2840 — `Packet_SMSG_GAMESPEED_SET`

- **Адрес (Offset):** `0x007e2840`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Game/ClientGameTime.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007e2840
static int32_t Packet_SMSG_GAMESPEED_SET(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007e2840 в IDA Pro / Ghidra
