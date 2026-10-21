---
offset: "0x00437640"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00437640 — `IOMpqArchiveUnit_IOMpqArchiveUnit`

- **Адрес (Offset):** `0x00437640`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00437640
IOMpqArchiveUnit::IOMpqArchiveUnit(System_SFile::ARCHIVEREC* archive, const char* name, uint32_t blockIndex, bool ownsMemory, IOUnit* next) : IOMpqUnit(archive, name, ownsMemory, next) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00437640 в IDA Pro / Ghidra
