---
offset: "0x006b0960"
module: "WoW/Source"
file: "WoW/Source/WowServices/RealmConnection.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b0960 — `RealmResponse_OnCharacterRestored`

- **Адрес (Offset):** `0x006b0960`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/RealmConnection.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b0960
void RealmResponse::OnCharacterRestored(RealmConnection* connection, bool success, uint32_t a3, uint32_t a4, uint32_t a5, uint64_t a6, uint64_t a7, uint32_t a8, const char* a9, uint32_t a10, CDataStore* msg, uint64_t a12, uint64_t a13) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b0960 в IDA Pro / Ghidra
