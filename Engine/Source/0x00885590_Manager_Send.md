---
offset: "0x00885590"
module: "Engine/Source"
file: "Engine/Source/ComSat/ComSatNetworkManager.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00885590 — `Manager_Send`

- **Адрес (Offset):** `0x00885590`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ComSat/ComSatNetworkManager.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00885590
bool ComSat::Network::Manager::Send(uint16_t networkId, uint8_t talker, const uint8_t (&key)[16], const ComSat::Network::Address& address, const uint8_t* data, uint32_t size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00885590 в IDA Pro / Ghidra
