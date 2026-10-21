---
offset: "0x00632060"
module: "WoW/Source"
file: "WoW/Source/Net/NetClient/NetClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00632060 — `NetClient_WCConnected`

- **Адрес (Offset):** `0x00632060`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Net/NetClient/NetClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00632060
void NetClient::WCConnected(WowConnection* connection, WowConnection* inbound, uint32_t timeStamp, const NETCONNADDR* addr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00632060 в IDA Pro / Ghidra
