---
offset: "0x006326d0"
module: "WoW/Source"
file: "WoW/Source/Net/NetClient/NetClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006326d0 — `NetClient_WCDisconnected`

- **Адрес (Offset):** `0x006326d0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Net/NetClient/NetClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006326d0
void NetClient::WCDisconnected(WowConnection* connection, uint32_t timeStamp, const NETCONNADDR* addr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006326d0 в IDA Pro / Ghidra
