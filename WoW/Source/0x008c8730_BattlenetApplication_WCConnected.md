---
offset: "0x008c8730"
module: "WoW/Source"
file: "WoW/Source/WowServices/BattlenetLogin.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008c8730 — `BattlenetApplication_WCConnected`

- **Адрес (Offset):** `0x008c8730`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/BattlenetLogin.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008c8730
void BattlenetApplication::WCConnected(WowConnection* connection, WowConnection* inbound, uint32_t timeStamp, const NETCONNADDR* addr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008c8730 в IDA Pro / Ghidra
