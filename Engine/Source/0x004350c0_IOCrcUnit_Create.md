---
offset: "0x004350c0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/iounit/IOChecksumUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004350c0 — `IOCrcUnit_Create`

- **Адрес (Offset):** `0x004350c0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/iounit/IOChecksumUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004350c0
IOUnit* IOCrcUnit::Create(IOUnitContainer* container, int64_t size, Callback callback, bool readToEnd, IOChecksumUnit** self, IOUnit* next) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004350c0 в IDA Pro / Ghidra
