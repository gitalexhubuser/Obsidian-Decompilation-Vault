---
offset: "0x00421a10"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/SFile2-Core.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00421a10 — `SFile_OpenPathAsArchive`

- **Адрес (Offset):** `0x00421a10`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/SFile2-Core.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00421a10
int32_t STORMAPI SFile::OpenPathAsArchive(SArchive* archive, const char* path, int32_t priority, uint32_t flags, SArchive** result) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00421a10 в IDA Pro / Ghidra
