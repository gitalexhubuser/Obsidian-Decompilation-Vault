---
offset: "0x00680c20"
module: "WoW/Source"
file: "WoW/Source/DB/DBClient/DBCacheInstances.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00680c20 — `ItemAdded`

- **Адрес (Offset):** `0x00680c20`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/DB/DBClient/DBCacheInstances.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00680c20
template <> void DBCache<NameCache, uint64_t, CHashKeyGUID>::ItemAdded(NameCache* item) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00680c20 в IDA Pro / Ghidra
