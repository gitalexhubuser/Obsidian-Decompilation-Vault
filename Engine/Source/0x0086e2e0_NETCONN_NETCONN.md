---
offset: "0x0086e2e0"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsTcp.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0086e2e0 — `NETCONN_NETCONN`

- **Адрес (Offset):** `0x0086e2e0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsTcp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0086e2e0
OsNet::NETCONN::NETCONN(TCPNET* net, SOCKET sock, NETEVENTPROC eventProc, void* user, const NETCONNADDR* connAddr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0086e2e0 в IDA Pro / Ghidra
