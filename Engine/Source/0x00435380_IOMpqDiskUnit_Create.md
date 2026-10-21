---
offset: "0x00435380"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00435380 — `IOMpqDiskUnit_Create`

- **Адрес (Offset):** `0x00435380`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00435380
IOMpqDiskUnit* IOMpqDiskUnit::Create(IOUnitContainer* container, System_SFile::ARCHIVEREC* archive, const char* name, const char* path, IOUnit* next) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00435380 в IDA Pro / Ghidra
