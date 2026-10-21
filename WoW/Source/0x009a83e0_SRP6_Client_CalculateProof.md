---
offset: "0x009a83e0"
module: "WoW/Source"
file: "WoW/Source/WowServices/SRP6_Client.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x009a83e0 — `SRP6_Client_CalculateProof`

- **Адрес (Offset):** `0x009a83e0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/SRP6_Client.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009a83e0
int32_t SRP6_Client::CalculateProof(const uint8_t* largeSafePrime, uint32_t largeSafePrimeLength, const uint8_t* generator, uint32_t generatorLength, const uint8_t* salt, uint32_t saltLength, const uint8_t* serverPublicKey, uint32_t serverPublicKeyLength, SRP6_Random& random) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x009a83e0 в IDA Pro / Ghidra
