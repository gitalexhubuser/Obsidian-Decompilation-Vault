---
offset: "0x00430650"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/iounit/IOAlignUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00430650 — `IOAlignUnit_IOAlignUnit`

- **Адрес (Offset):** `0x00430650`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/iounit/IOAlignUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00430650
IOAlignUnit::IOAlignUnit(int64_t base, uint32_t blockSize, uint32_t blockCount, bool largeTransfers, bool exactSize, uint32_t bufferAlign, bool skipCleanOnWrite, int64_t size, bool ownsMemory, IOUnit* next) : IOUnit(next, ownsMemory) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00430650 в IDA Pro / Ghidra
