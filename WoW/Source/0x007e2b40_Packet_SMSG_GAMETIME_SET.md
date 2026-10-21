---
offset: "0x007e2b40"
module: "WoW/Source"
file: "WoW/Source/Game/ClientGameTime.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007e2b40 — `Packet_SMSG_GAMETIME_SET`

- **Адрес (Offset):** `0x007e2b40`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Game/ClientGameTime.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007e2b40
static int32_t Packet_SMSG_GAMETIME_SET(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007e2b40 в IDA Pro / Ghidra
