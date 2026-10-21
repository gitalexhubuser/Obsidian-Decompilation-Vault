---
offset: "0x00404a80"
module: "WoW/Source"
file: "WoW/Source/Client.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00404a80 — `ListInterfaceArchive`

- **Адрес (Offset):** `0x00404a80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Client.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00404a80
void ListInterfaceArchive(const char* prefix, int32_t (*callback)(const char* fileName, void* param), void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00404a80 в IDA Pro / Ghidra
