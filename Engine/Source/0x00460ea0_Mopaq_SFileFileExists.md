---
offset: "0x00460ea0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00460ea0 — `Mopaq_SFileFileExists`

- **Адрес (Offset):** `0x00460ea0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00460ea0
int32_t Blizzard::Mopaq::SFileFileExists(System_SFile::ARCHIVEREC* handle, const char* name, uint32_t flags, System_SFile::ARCHIVEREC** archiveOut) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00460ea0 в IDA Pro / Ghidra
