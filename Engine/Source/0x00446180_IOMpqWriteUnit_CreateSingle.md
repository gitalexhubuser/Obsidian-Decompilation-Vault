---
offset: "0x00446180"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00446180 — `IOMpqWriteUnit_CreateSingle`

- **Адрес (Offset):** `0x00446180`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00446180
IOUnit* IOMpqWriteUnit::CreateSingle(IOUnitContainer* container, const std::vector<Blizzard::Mopaq::CompressionAlgorithm>& compression, uint32_t fileSize, Callback callback, IOMpqWriteUnit** self, IOUnit* next) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00446180 в IDA Pro / Ghidra
