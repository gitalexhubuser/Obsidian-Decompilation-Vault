---
offset: "0x006b2000"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b2000 — `ClientRealmResponseAdapter_CharacterListReceived`

- **Адрес (Offset):** `0x006b2000`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b2000
void ClientRealmResponseAdapter::CharacterListReceived(RealmConnection* connection, const TSFixedArray<CHARACTER_INFO>& characters, int32_t success) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b2000 в IDA Pro / Ghidra
