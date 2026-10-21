---
offset: "0x009c2900"
module: "WoW/Source"
file: "WoW/Source/Battlenet/Win64/Battlenet.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x009c2900 — `Library_Load`

- **Адрес (Offset):** `0x009c2900`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/Win64/Battlenet.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009c2900
Battlenet::Library* Battlenet::Library::Load(const char* path, Allocator& allocator) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x009c2900 в IDA Pro / Ghidra
