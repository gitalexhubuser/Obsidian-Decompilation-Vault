---
offset: "0x007e2a50"
module: "WoW/Source"
file: "WoW/Source/Game/ClientGameTime.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007e2a50 — `Packet_SMSG_SERVERTIME`

- **Адрес (Offset):** `0x007e2a50`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Game/ClientGameTime.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007e2a50
static int32_t Packet_SMSG_SERVERTIME(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007e2a50 в IDA Pro / Ghidra
