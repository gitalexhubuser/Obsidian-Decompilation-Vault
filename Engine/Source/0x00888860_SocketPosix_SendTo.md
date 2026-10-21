---
offset: "0x00888860"
module: "Engine/Source"
file: "Engine/Source/ComSat/Win64/ComSatNetworkSocketPosix.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00888860 — `SocketPosix_SendTo`

- **Адрес (Offset):** `0x00888860`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ComSat/Win64/ComSatNetworkSocketPosix.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00888860
int32_t ComSat::Network::SocketPosix::SendTo(const ComSat::Network::Address& address, const uint8_t* data, uint32_t size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00888860 в IDA Pro / Ghidra
