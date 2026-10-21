---
offset: "0x008853d0"
module: "Engine/Source"
file: "Engine/Source/ComSat/ComSatNetworkManager.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008853d0 — `Manager_Manager`

- **Адрес (Offset):** `0x008853d0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ComSat/ComSatNetworkManager.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008853d0
ComSat::Network::Manager::Manager(const ComSat::Initialization& init, ComSat::Allocator& allocator) : m_allocator(&allocator), m_sessions(allocator) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008853d0 в IDA Pro / Ghidra
