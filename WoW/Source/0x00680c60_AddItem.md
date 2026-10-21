---
offset: "0x00680c60"
module: "WoW/Source"
file: "WoW/Source/DB/DBClient/DBCacheInstances.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00680c60 — `AddItem`

- **Адрес (Offset):** `0x00680c60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/DB/DBClient/DBCacheInstances.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00680c60
template <> void DBCache<NameCache, uint64_t, CHashKeyGUID>::AddItem(NameCache* item, uint64_t key) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00680c60 в IDA Pro / Ghidra
