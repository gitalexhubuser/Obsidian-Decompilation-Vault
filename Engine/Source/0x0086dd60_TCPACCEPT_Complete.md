---
offset: "0x0086dd60"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsTcp.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0086dd60 — `TCPACCEPT_Complete`

- **Адрес (Offset):** `0x0086dd60`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsTcp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0086dd60
SOCKET OsNet::TCPACCEPT::Complete(NETCONNADDR* connAddr, int32_t makeSock) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0086dd60 в IDA Pro / Ghidra
