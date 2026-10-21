---
offset: "0x00424fa0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/SFile2-Core.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00424fa0 — `SFile_List`

- **Адрес (Offset):** `0x00424fa0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/SFile2-Core.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00424fa0
int32_t STORMAPI SFile::List(SArchive* archive, int32_t (*callback)(const char* fileName, void* param), void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00424fa0 в IDA Pro / Ghidra
