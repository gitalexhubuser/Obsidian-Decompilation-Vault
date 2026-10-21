---
offset: "0x0086eaf0"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsTcp.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0086eaf0 — `TCPCONN_CompleteWrite`

- **Адрес (Offset):** `0x0086eaf0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsTcp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0086eaf0
void OsNet::TCPCONN::CompleteWrite(NETOVERLAP* overlap, uint32_t bytes) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0086eaf0 в IDA Pro / Ghidra
