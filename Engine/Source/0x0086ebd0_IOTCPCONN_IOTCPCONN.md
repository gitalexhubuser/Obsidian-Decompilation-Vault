---
offset: "0x0086ebd0"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsTcp.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0086ebd0 — `IOTCPCONN_IOTCPCONN`

- **Адрес (Offset):** `0x0086ebd0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsTcp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0086ebd0
OsNet::IOTCPCONN::IOTCPCONN(TCPNET* net, HANDLE port, SOCKET sock, NETEVENTPROC eventProc, void* user, const NETCONNADDR* connAddr, const void* data, uint32_t bytes) : TCPCONN(net, sock, eventProc, user, connAddr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0086ebd0 в IDA Pro / Ghidra
