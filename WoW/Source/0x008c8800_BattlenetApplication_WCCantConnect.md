---
offset: "0x008c8800"
module: "WoW/Source"
file: "WoW/Source/WowServices/BattlenetLogin.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008c8800 — `BattlenetApplication_WCCantConnect`

- **Адрес (Offset):** `0x008c8800`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/BattlenetLogin.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008c8800
void BattlenetApplication::WCCantConnect(WowConnection* connection, uint32_t timeStamp, const NETCONNADDR* addr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008c8800 в IDA Pro / Ghidra
