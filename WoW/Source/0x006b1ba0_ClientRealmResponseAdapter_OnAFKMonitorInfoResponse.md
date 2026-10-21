---
offset: "0x006b1ba0"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b1ba0 — `ClientRealmResponseAdapter_OnAFKMonitorInfoResponse`

- **Адрес (Offset):** `0x006b1ba0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b1ba0
void ClientRealmResponseAdapter::OnAFKMonitorInfoResponse(RealmConnection* connection, WOWGUID guid, int32_t unused_a3, int32_t unused_a4, int32_t unused_a5, int32_t unused_a6) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b1ba0 в IDA Pro / Ghidra
