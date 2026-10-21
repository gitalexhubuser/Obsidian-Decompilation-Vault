---
offset: "0x0086e550"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsTcp.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0086e550 — `TCPCONN_TCPCONN`

- **Адрес (Offset):** `0x0086e550`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsTcp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0086e550
OsNet::TCPCONN::TCPCONN(TCPNET* net, SOCKET sock, NETEVENTPROC eventProc, void* user, const NETCONNADDR* connAddr) : NETCONNFULL(net, sock, eventProc, user, connAddr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0086e550 в IDA Pro / Ghidra
