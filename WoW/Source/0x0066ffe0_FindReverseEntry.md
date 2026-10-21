---
offset: "0x0066ffe0"
module: "WoW/Source"
file: "WoW/Source/DB/DBClient/DBCacheInstances.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0066ffe0 — `FindReverseEntry`

- **Адрес (Offset):** `0x0066ffe0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/DB/DBClient/DBCacheInstances.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0066ffe0
template <> DBCache<NameCache, uint64_t, CHashKeyGUID>::REVERSEENTRY* DBCache<NameCache, uint64_t, CHashKeyGUID>::FindReverseEntry(const char* name) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0066ffe0 в IDA Pro / Ghidra
