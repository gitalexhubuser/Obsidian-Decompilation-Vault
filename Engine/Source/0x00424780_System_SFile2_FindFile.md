---
offset: "0x00424780"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/SFile2-Core.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00424780 — `System_SFile2_FindFile`

- **Адрес (Offset):** `0x00424780`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/SFile2-Core.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00424780
bool System_SFile2::FindFile(const char* name, char* path, uint32_t size, uint32_t flags, SFILE_TYPE* type, System_SFile::ARCHIVEREC** archive) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00424780 в IDA Pro / Ghidra
