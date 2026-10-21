---
offset: "0x00467990"
module: "WoW/Source"
file: "WoW/Source/WowServices/Win64/WowConnection.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00467990 — `WowConnection_Send`

- **Адрес (Offset):** `0x00467990`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/Win64/WowConnection.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00467990
WC_SEND_RESULT WowConnection::Send(uint8_t* data, int32_t size, bool raw) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00467990 в IDA Pro / Ghidra
