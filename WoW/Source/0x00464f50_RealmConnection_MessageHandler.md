---
offset: "0x00464f50"
module: "WoW/Source"
file: "WoW/Source/WowServices/RealmConnection.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00464f50 — `RealmConnection_MessageHandler`

- **Адрес (Offset):** `0x00464f50`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/RealmConnection.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00464f50
int32_t RealmConnection::MessageHandler(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00464f50 в IDA Pro / Ghidra
