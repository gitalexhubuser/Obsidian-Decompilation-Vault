---
offset: "0x0086ee00"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsTcp.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0086ee00 — `TCPNET_TcpMakeConn`

- **Адрес (Offset):** `0x0086ee00`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsTcp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0086ee00
void OsNet::TCPNET::TcpMakeConn(SOCKET sock, NETEVENTPROC eventProc, void* user, const NETCONNADDR* connAddr, const void* data, uint32_t bytes) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0086ee00 в IDA Pro / Ghidra
