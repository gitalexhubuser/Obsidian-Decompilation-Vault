---
offset: "0x00460f00"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00460f00 — `Mopaq_SFileGetFileDetails`

- **Адрес (Offset):** `0x00460f00`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00460f00
bool Blizzard::Mopaq::SFileGetFileDetails(System_SFile::ARCHIVEREC* handle, const char* name, System_SFile::ARCHIVEREC** archiveOut, int64_t* offset, uint32_t* size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00460f00 в IDA Pro / Ghidra
