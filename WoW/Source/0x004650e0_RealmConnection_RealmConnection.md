---
offset: "0x004650e0"
module: "WoW/Source"
file: "WoW/Source/WowServices/RealmConnection.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004650e0 — `RealmConnection_RealmConnection`

- **Адрес (Offset):** `0x004650e0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/RealmConnection.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004650e0
RealmConnection::RealmConnection(RealmResponse* realmResponse) : m_realmResponse(realmResponse), m_authenticated(0), m_queuePosition(0), m_freeCharacterMigration(0), m_billingTimeRemaining(0), m_billingTimeRested(0), m_billingFlags(0), m_accountExpansion(0), m_regionId(0), m_battlegroupId(0), m_realmId(0) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004650e0 в IDA Pro / Ghidra
