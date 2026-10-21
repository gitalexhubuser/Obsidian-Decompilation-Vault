---
offset: "0x00574d00"
module: "WoW/Source"
file: "WoW/Source/Ui/RaidInfo.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00574d00 — `ReadyCheckNameCallback`

- **Адрес (Offset):** `0x00574d00`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/RaidInfo.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00574d00
static void ReadyCheckNameCallback(int32_t id, const WOWGUID& guid, void* param, bool success) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00574d00 в IDA Pro / Ghidra
