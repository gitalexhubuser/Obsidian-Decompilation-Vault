---
offset: "0x00632c10"
module: "WoW/Source"
file: "WoW/Source/Net/NetClient/NetClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00632c10 — `NetClient_WCCantConnect`

- **Адрес (Offset):** `0x00632c10`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Net/NetClient/NetClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00632c10
void NetClient::WCCantConnect(WowConnection* connection, uint32_t timeStamp, const NETCONNADDR* addr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00632c10 в IDA Pro / Ghidra
