---
offset: "0x00888fb0"
module: "WoW/Source"
file: "WoW/Source/Battlenet/BSN/BSNCpp.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00888fb0 — `BSN_UTF8StringCopy`

- **Адрес (Offset):** `0x00888fb0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/BSN/BSNCpp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00888fb0
uint32_t BSN::UTF8StringCopy(char* dest, const char* source, uint32_t maxChars, uint32_t& length) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00888fb0 в IDA Pro / Ghidra
