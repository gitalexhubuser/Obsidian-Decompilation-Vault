---
offset: "0x004396e0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004396e0 — `IOMpqArchiveReadUnit_Create`

- **Адрес (Offset):** `0x004396e0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004396e0
IOMpqArchiveReadUnit* IOMpqArchiveReadUnit::Create(IOUnitContainer* container, System_SFile::ARCHIVEREC* archive, const char* name, uint32_t blockIndex, IOUnit* next) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004396e0 в IDA Pro / Ghidra
