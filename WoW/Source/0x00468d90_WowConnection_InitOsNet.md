---
offset: "0x00468d90"
module: "WoW/Source"
file: "WoW/Source/WowServices/WowConnection.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00468d90 — `WowConnection_InitOsNet`

- **Адрес (Offset):** `0x00468d90`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/WowConnection.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00468d90
int32_t WowConnection::InitOsNet(bool (*netAddrFilter)(const NETADDR* addr), void (*threadInit)(), int32_t numThreads, bool useEngine) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00468d90 в IDA Pro / Ghidra
