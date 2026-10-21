---
offset: "0x00434b90"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/iounit/IOAlignUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00434b90 — `IOAlignUnit_Create`

- **Адрес (Offset):** `0x00434b90`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/iounit/IOAlignUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00434b90
IOAlignUnit* IOAlignUnit::Create(IOUnitContainer* container, int64_t base, uint32_t blockSize, uint32_t blockCount, bool largeTransfers, bool exactSize, uint32_t bufferAlign, bool skipCleanOnWrite, IOUnit* next) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00434b90 в IDA Pro / Ghidra
