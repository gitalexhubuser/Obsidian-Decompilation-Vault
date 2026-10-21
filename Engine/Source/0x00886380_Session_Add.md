---
offset: "0x00886380"
module: "Engine/Source"
file: "Engine/Source/ComSat/ComSatNetworkSession.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00886380 — `Session_Add`

- **Адрес (Offset):** `0x00886380`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ComSat/ComSatNetworkSession.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00886380
bool ComSat::Network::Session::Add(uint64_t talker, uint8_t networkId, const uint8_t (&key)[16], const ComSat::Network::Address& address) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00886380 в IDA Pro / Ghidra
