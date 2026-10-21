---
offset: "0x006b1b90"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b1b90 — `ClientRealmResponseAdapter_OnChatReceived`

- **Адрес (Offset):** `0x006b1b90`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b1b90
void ClientRealmResponseAdapter::OnChatReceived(RealmConnection* connection, WOWGUID guid, const char* text, uint8_t type) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b1b90 в IDA Pro / Ghidra
