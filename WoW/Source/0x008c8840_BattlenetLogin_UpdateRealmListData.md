---
offset: "0x008c8840"
module: "WoW/Source"
file: "WoW/Source/WowServices/BattlenetLogin.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008c8840 — `BattlenetLogin_UpdateRealmListData`

- **Адрес (Offset):** `0x008c8840`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/BattlenetLogin.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008c8840
void BattlenetLogin::UpdateRealmListData(uint32_t region, uint32_t battlegroup, uint32_t id, const Battlenet::Realm::Info* info, uint8_t flags, bool remove) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008c8840 в IDA Pro / Ghidra
