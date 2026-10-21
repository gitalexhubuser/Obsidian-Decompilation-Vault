---
offset: "0x00443ac0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00443ac0 — `IOMpqWriteUnit_IOMpqWriteUnit`

- **Адрес (Offset):** `0x00443ac0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00443ac0
IOMpqWriteUnit::IOMpqWriteUnit(const std::vector<Blizzard::Mopaq::CompressionAlgorithm>& compression, uint32_t fileSize, uint32_t sectorCount, uint32_t sectorSize, Callback callback, IOMpqWriteUnit** self, bool ownsMemory, IOUnit* next) : IOUnit(next, ownsMemory), m_checksums(sectorCount), m_sectorOffsets(sectorCount + 2), m_compression(compression) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00443ac0 в IDA Pro / Ghidra
