---
offset: "0x009c0210"
module: "WoW/Source"
file: "WoW/Source/Battlenet/BattlenetMap.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x009c0210 — `MapKey_MapKey`

- **Адрес (Offset):** `0x009c0210`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/BattlenetMap.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009c0210
Battlenet::MapKey::MapKey(const char* value) : MapKey(String(value)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x009c0210 в IDA Pro / Ghidra
