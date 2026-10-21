---
offset: "0x008cccb0"
module: "WoW/Source"
file: "WoW/Source/WowServices/Grunt.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008cccb0 — `ClientLink_WCConnected`

- **Адрес (Offset):** `0x008cccb0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/Grunt.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008cccb0
void Grunt::ClientLink::WCConnected(WowConnection* connection, WowConnection* inbound, uint32_t timeStamp, const NETCONNADDR* addr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008cccb0 в IDA Pro / Ghidra
