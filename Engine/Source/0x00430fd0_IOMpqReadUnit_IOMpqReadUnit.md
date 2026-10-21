---
offset: "0x00430fd0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00430fd0 — `IOMpqReadUnit_IOMpqReadUnit`

- **Адрес (Offset):** `0x00430fd0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00430fd0
IOMpqReadUnit::IOMpqReadUnit(uint32_t fileSize, uint32_t compressedSize, uint32_t flags, uint32_t key, bool ownsMemory, IOUnit* next) : IOUnit(next, ownsMemory), m_sectorOffsets(3), m_checksums(0) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00430fd0 в IDA Pro / Ghidra
