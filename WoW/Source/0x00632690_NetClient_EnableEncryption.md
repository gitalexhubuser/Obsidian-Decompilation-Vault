---
offset: "0x00632690"
module: "WoW/Source"
file: "WoW/Source/Net/NetClient/NetClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00632690 — `NetClient_EnableEncryption`

- **Адрес (Offset):** `0x00632690`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Net/NetClient/NetClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00632690
void NetClient::EnableEncryption(WowConnection* connection, const uint8_t* seed, uint8_t seedLength) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00632690 в IDA Pro / Ghidra
