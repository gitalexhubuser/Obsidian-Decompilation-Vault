---
offset: "0x008852e0"
module: "Engine/Source"
file: "Engine/Source/ComSat/ComSatNetworkManager.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008852e0 — `Network_ComputeSignature`

- **Адрес (Offset):** `0x008852e0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ComSat/ComSatNetworkManager.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008852e0
uint32_t ComSat::Network::ComputeSignature(const uint8_t (&key)[16], const uint8_t* data, uint32_t size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008852e0 в IDA Pro / Ghidra
