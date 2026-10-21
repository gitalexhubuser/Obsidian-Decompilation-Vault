---
offset: "0x0086e5d0"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsTcp.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0086e5d0 — `TCPCONN_LockedEnqueue`

- **Адрес (Offset):** `0x0086e5d0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsTcp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0086e5d0
OsNet::OUTPUT* OsNet::TCPCONN::LockedEnqueue(const void* data, uint32_t bytes) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0086e5d0 в IDA Pro / Ghidra
