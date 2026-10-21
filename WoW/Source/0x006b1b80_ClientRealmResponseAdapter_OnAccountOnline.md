---
offset: "0x006b1b80"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b1b80 — `ClientRealmResponseAdapter_OnAccountOnline`

- **Адрес (Offset):** `0x006b1b80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b1b80
void ClientRealmResponseAdapter::OnAccountOnline(RealmConnection* connection, int32_t unused_a2, WOWGUID guid) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b1b80 в IDA Pro / Ghidra
