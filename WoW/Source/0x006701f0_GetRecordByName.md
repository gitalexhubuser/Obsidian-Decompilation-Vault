---
offset: "0x006701f0"
module: "WoW/Source"
file: "WoW/Source/DB/DBClient/DBCacheInstances.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006701f0 — `GetRecordByName`

- **Адрес (Offset):** `0x006701f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/DB/DBClient/DBCacheInstances.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006701f0
template <> PetNameCache* DBCache<PetNameCache, int32_t, HASHKEY_INT>::GetRecordByName(const char* name) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006701f0 в IDA Pro / Ghidra
