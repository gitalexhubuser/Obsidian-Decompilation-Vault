---
offset: "0x004034f0"
module: "WoW/Source"
file: "WoW/Source/Client.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004034f0 — `SendErrorLog`

- **Адрес (Offset):** `0x004034f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Client.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004034f0
int32_t STORMAPI SendErrorLog(uint32_t errorcode, const char* description, const char* filename, int32_t linenumber, const char* errorstring) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004034f0 в IDA Pro / Ghidra
