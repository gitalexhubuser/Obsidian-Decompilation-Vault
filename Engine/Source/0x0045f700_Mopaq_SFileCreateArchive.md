---
offset: "0x0045f700"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0045f700 — `Mopaq_SFileCreateArchive`

- **Адрес (Offset):** `0x0045f700`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0045f700
bool Blizzard::Mopaq::SFileCreateArchive(const char* path, int32_t priority, uint32_t userDataSize, System_SFile::ARCHIVEREC** result, const ArchiveOptions* options) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0045f700 в IDA Pro / Ghidra
