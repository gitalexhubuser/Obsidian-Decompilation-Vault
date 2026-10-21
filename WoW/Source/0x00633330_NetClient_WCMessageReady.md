---
offset: "0x00633330"
module: "WoW/Source"
file: "WoW/Source/Net/NetClient/NetClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00633330 — `NetClient_WCMessageReady`

- **Адрес (Offset):** `0x00633330`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Net/NetClient/NetClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00633330
void NetClient::WCMessageReady(WowConnection* connection, uint32_t timeStamp, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00633330 в IDA Pro / Ghidra
