---
offset: "0x00888890"
module: "Engine/Source"
file: "Engine/Source/ComSat/Win64/ComSatNetworkSocketPosix.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00888890 — `SocketPosix_RecvFrom`

- **Адрес (Offset):** `0x00888890`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ComSat/Win64/ComSatNetworkSocketPosix.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00888890
bool ComSat::Network::SocketPosix::RecvFrom(ComSat::Network::Address& address, uint8_t* data, uint32_t& size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00888890 в IDA Pro / Ghidra
