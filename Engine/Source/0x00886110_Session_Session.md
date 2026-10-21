---
offset: "0x00886110"
module: "Engine/Source"
file: "Engine/Source/ComSat/ComSatNetworkSession.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00886110 — `Session_Session`

- **Адрес (Offset):** `0x00886110`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ComSat/ComSatNetworkSession.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00886110
ComSat::Network::Session::Session(ComSat::Network::Manager& manager, uint64_t id, ComSat::Network::Session::Callback& callback) : m_localTalkers(*manager.m_allocator), m_endpoints(*manager.m_allocator), m_remoteTalkers(*manager.m_allocator) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00886110 в IDA Pro / Ghidra
