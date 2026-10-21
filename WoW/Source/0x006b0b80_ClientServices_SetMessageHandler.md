---
offset: "0x006b0b80"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b0b80 — `ClientServices_SetMessageHandler`

- **Адрес (Offset):** `0x006b0b80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b0b80
void ClientServices::SetMessageHandler(NETMESSAGE msgId, MESSAGE_HANDLER handler, void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b0b80 в IDA Pro / Ghidra
