---
offset: "0x006bb390"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/CheckExecutableSignature.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006bb390 — `GetDllVersionString`

- **Адрес (Offset):** `0x006bb390`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/CheckExecutableSignature.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006bb390
bool GetDllVersionString(const char* fileName, char* buffer, uint32_t size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006bb390 в IDA Pro / Ghidra
