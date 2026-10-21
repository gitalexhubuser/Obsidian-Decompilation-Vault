---
offset: "0x00443c90"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00443c90 — `IOMpqWriteUnit_IOMpqWriteUnit`

- **Адрес (Offset):** `0x00443c90`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00443c90
IOMpqWriteUnit::IOMpqWriteUnit(const std::vector<Blizzard::Mopaq::CompressionAlgorithm>& compression, uint32_t fileSize, Callback callback, IOMpqWriteUnit** self, bool ownsMemory, IOUnit* next) : IOUnit(next, ownsMemory), m_checksums(0), m_sectorOffsets(0), m_compression(compression) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00443c90 в IDA Pro / Ghidra
