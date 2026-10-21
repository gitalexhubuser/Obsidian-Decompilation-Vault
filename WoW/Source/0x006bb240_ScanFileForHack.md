---
offset: "0x006bb240"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/CheckExecutableSignature.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006bb240 — `ScanFileForHack`

- **Адрес (Offset):** `0x006bb240`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/CheckExecutableSignature.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006bb240
bool ScanFileForHack(const char* fileName, uint8_t* hackFound, uint8_t* shouldBlockPlaying, const char** result, char* hackName, uint32_t hackNameSize) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006bb240 в IDA Pro / Ghidra
