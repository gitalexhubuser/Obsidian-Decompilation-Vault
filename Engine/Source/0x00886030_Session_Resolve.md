---
offset: "0x00886030"
module: "Engine/Source"
file: "Engine/Source/ComSat/ComSatNetworkSession.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00886030 — `Session_Resolve`

- **Адрес (Offset):** `0x00886030`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ComSat/ComSatNetworkSession.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00886030
bool ComSat::Network::Session::Resolve(uint8_t networkId, const ComSat::Network::Address& address, uint64_t& talker, const uint8_t (*&key)[16]) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00886030 в IDA Pro / Ghidra
