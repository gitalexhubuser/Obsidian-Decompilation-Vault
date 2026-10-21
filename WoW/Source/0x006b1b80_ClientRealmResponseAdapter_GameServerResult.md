---
offset: "0x006b1b80"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b1b80 — `ClientRealmResponseAdapter_GameServerResult`

- **Адрес (Offset):** `0x006b1b80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b1b80
void ClientRealmResponseAdapter::GameServerResult(RealmConnection* connection, const char* message1, const char* message2, const char* message3) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b1b80 в IDA Pro / Ghidra
