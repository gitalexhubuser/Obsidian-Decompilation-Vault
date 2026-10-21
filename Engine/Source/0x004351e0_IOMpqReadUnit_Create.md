---
offset: "0x004351e0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004351e0 — `IOMpqReadUnit_Create`

- **Адрес (Offset):** `0x004351e0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004351e0
IOUnit* IOMpqReadUnit::Create(IOUnitContainer* container, uint32_t fileSize, uint32_t compressedSize, uint32_t sectorSize, uint32_t flags, uint32_t key, IOUnit* next) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004351e0 в IDA Pro / Ghidra
