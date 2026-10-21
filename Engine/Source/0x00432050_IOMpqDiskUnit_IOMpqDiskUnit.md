---
offset: "0x00432050"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00432050 — `IOMpqDiskUnit_IOMpqDiskUnit`

- **Адрес (Offset):** `0x00432050`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00432050
IOMpqDiskUnit::IOMpqDiskUnit(System_SFile::ARCHIVEREC* archive, const char* name, const char* path, bool ownsMemory, IOUnit* next) : IOMpqUnit(archive, name, ownsMemory, next), m_path((path ? static_cast<uint32_t>(strlen(path)) : 0) + 1) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00432050 в IDA Pro / Ghidra
