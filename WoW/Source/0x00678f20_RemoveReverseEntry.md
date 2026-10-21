---
offset: "0x00678f20"
module: "WoW/Source"
file: "WoW/Source/DB/DBClient/DBCacheInstances.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00678f20 — `RemoveReverseEntry`

- **Адрес (Offset):** `0x00678f20`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/DB/DBClient/DBCacheInstances.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00678f20
template <> void DBCache<NameCache, uint64_t, CHashKeyGUID>::RemoveReverseEntry(const char* name) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00678f20 в IDA Pro / Ghidra
