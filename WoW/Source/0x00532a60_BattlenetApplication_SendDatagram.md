---
offset: "0x00532a60"
module: "WoW/Source"
file: "WoW/Source/WowServices/BattlenetLogin.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00532a60 — `BattlenetApplication_SendDatagram`

- **Адрес (Offset):** `0x00532a60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/BattlenetLogin.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00532a60
bool BattlenetApplication::SendDatagram(uint32_t connection, const void* data, uint32_t size, const Battlenet::IP4::AddressPort& address) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00532a60 в IDA Pro / Ghidra
