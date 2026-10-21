---
offset: "0x004675f0"
module: "WoW/Source"
file: "WoW/Source/WowServices/Win64/WowConnection.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004675f0 — `WowConnection_SendPacket`

- **Адрес (Offset):** `0x004675f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/Win64/WowConnection.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004675f0
WC_SEND_RESULT WowConnection::SendPacket(CDataStore* msg, int32_t headroom) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004675f0 в IDA Pro / Ghidra
