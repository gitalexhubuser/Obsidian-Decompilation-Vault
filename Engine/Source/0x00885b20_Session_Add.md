---
offset: "0x00885b20"
module: "Engine/Source"
file: "Engine/Source/ComSat/ComSatSession.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00885b20 — `Session_Add`

- **Адрес (Offset):** `0x00885b20`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ComSat/ComSatSession.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00885b20
bool ComSat::Session::Add(uint64_t talker, uint8_t networkId, const uint8_t (&key)[16], const ComSat::Network::Address& address) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00885b20 в IDA Pro / Ghidra
