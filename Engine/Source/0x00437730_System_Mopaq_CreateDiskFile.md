---
offset: "0x00437730"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00437730 — `System_Mopaq_CreateDiskFile`

- **Адрес (Offset):** `0x00437730`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00437730
bool System_Mopaq::CreateDiskFile(const char* name, uint32_t flags, const char* path, System_SFile::ARCHIVEREC* archive, IOMpqUnit** result) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00437730 в IDA Pro / Ghidra
