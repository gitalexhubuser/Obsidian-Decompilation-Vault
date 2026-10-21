---
offset: "0x006b0870"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b0870 — `ClientConnection_AccountLogin`

- **Адрес (Offset):** `0x006b0870`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b0870
void ClientConnection::AccountLogin(const char* accountName, const char* password, int32_t region, int32_t locale) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b0870 в IDA Pro / Ghidra
