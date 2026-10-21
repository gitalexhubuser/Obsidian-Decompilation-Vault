---
offset: "0x00434ce0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/iounit/Win64/IOFileUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00434ce0 — `IOUnbufferedFileUnit_IOUnbufferedFileUnit`

- **Адрес (Offset):** `0x00434ce0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/iounit/Win64/IOFileUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00434ce0
IOUnbufferedFileUnit::IOUnbufferedFileUnit(Blizzard::File::StreamRecord* stream, bool ownsMemory) : IOFileUnit(stream, ownsMemory) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00434ce0 в IDA Pro / Ghidra
