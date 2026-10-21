---
offset: "0x00403380"
module: "WoW/Source"
file: "WoW/Source/Client.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00403380 — `ClientSetTimer`

- **Адрес (Offset):** `0x00403380`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Client.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00403380
uint32_t ClientSetTimer(uint32_t delay, EVENTHANDLERGUIDFUNC handler, uint64_t guid, void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00403380 в IDA Pro / Ghidra
