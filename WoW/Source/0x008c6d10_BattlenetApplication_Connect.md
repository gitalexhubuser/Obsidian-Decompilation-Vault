---
offset: "0x008c6d10"
module: "WoW/Source"
file: "WoW/Source/WowServices/BattlenetLogin.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008c6d10 — `BattlenetApplication_Connect`

- **Адрес (Offset):** `0x008c6d10`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/BattlenetLogin.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008c6d10
uint32_t BattlenetApplication::Connect(const Battlenet::IP4::AddressPort& address, const uint32_t& tendrilId) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008c6d10 в IDA Pro / Ghidra
