---
offset: "0x0086d800"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsTcp.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0086d800 — `TCPCONN_CompleteRead`

- **Адрес (Offset):** `0x0086d800`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsTcp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0086d800
void OsNet::TCPCONN::CompleteRead(NETOVERLAP* overlap, uint32_t bytes) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0086d800 в IDA Pro / Ghidra
