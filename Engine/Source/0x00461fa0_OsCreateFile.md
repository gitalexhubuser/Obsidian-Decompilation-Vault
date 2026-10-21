---
offset: "0x00461fa0"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsFile.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00461fa0 — `OsCreateFile`

- **Адрес (Offset):** `0x00461fa0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsFile.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00461fa0
HOSFILE OsCreateFile(const char* fileName, uint32_t desiredAccess, uint32_t shareMode, uint32_t createDisposition, uint32_t flagsAndAttributes, uint32_t extendedFileType) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00461fa0 в IDA Pro / Ghidra
