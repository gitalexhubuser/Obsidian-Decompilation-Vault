---
offset: "0x004397b0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004397b0 — `IOMpqArchiveWriteUnit_Create`

- **Адрес (Offset):** `0x004397b0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004397b0
IOMpqArchiveWriteUnit* IOMpqArchiveWriteUnit::Create(IOUnitContainer* container, System_SFile::ARCHIVEREC* archive, const char* name, uint32_t blockIndex, IOUnit* next) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004397b0 в IDA Pro / Ghidra
