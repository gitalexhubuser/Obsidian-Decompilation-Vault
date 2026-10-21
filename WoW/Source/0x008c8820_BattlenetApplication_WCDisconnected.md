---
offset: "0x008c8820"
module: "WoW/Source"
file: "WoW/Source/WowServices/BattlenetLogin.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008c8820 — `BattlenetApplication_WCDisconnected`

- **Адрес (Offset):** `0x008c8820`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/BattlenetLogin.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008c8820
void BattlenetApplication::WCDisconnected(WowConnection* connection, uint32_t timeStamp, const NETCONNADDR* addr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008c8820 в IDA Pro / Ghidra
