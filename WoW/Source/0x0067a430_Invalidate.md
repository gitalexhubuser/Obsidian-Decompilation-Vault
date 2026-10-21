---
offset: "0x0067a430"
module: "WoW/Source"
file: "WoW/Source/DB/DBClient/DBCacheInstances.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0067a430 — `Invalidate`

- **Адрес (Offset):** `0x0067a430`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/DB/DBClient/DBCacheInstances.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0067a430
template <> void DBCache<NameCache, uint64_t, CHashKeyGUID>::Invalidate(uint64_t key) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0067a430 в IDA Pro / Ghidra
