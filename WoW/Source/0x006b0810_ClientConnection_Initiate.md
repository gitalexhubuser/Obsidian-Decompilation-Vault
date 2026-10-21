---
offset: "0x006b0810"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b0810 — `ClientConnection_Initiate`

- **Адрес (Offset):** `0x006b0810`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b0810
void ClientConnection::Initiate(WOWCS_OPS op, int32_t errorCode, void (*cleanup)()) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b0810 в IDA Pro / Ghidra
