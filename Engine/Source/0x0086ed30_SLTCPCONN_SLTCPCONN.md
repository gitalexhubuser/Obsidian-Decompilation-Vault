---
offset: "0x0086ed30"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsTcp.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0086ed30 — `SLTCPCONN_SLTCPCONN`

- **Адрес (Offset):** `0x0086ed30`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsTcp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0086ed30
OsNet::SLTCPCONN::SLTCPCONN(TCPNET* net, SOCKET sock, NETEVENTPROC eventProc, void* user, const NETCONNADDR* connAddr, const void* data, uint32_t bytes) : TCPCONN(net, sock, eventProc, user, connAddr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0086ed30 в IDA Pro / Ghidra
