---
offset: "0x004460d0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004460d0 — `IOMpqWriteUnit_Create`

- **Адрес (Offset):** `0x004460d0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004460d0
IOUnit* IOMpqWriteUnit::Create(IOUnitContainer* container, const std::vector<Blizzard::Mopaq::CompressionAlgorithm>& compression, uint32_t fileSize, uint32_t sectorSize, Callback callback, IOMpqWriteUnit** self, IOUnit* next) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004460d0 в IDA Pro / Ghidra
