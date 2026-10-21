---
offset: "0x00435180"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/iounit/IOChecksumUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00435180 — `IOMd5Unit_Create`

- **Адрес (Offset):** `0x00435180`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/iounit/IOChecksumUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00435180
IOUnit* IOMd5Unit::Create(IOUnitContainer* container, int64_t size, Callback callback, bool readToEnd, IOChecksumUnit** self, IOUnit* next) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00435180 в IDA Pro / Ghidra
