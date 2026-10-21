---
offset: "0x006337d0"
module: "WoW/Source"
file: "WoW/Source/DB/DBClient/DBClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006337d0 — `StaticDBLoadAll`

- **Адрес (Offset):** `0x006337d0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/DB/DBClient/DBClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006337d0
static void StaticDBLoadAll(void (WowClientDB_Base::*loadFunction)(const char*, int32_t)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006337d0 в IDA Pro / Ghidra
