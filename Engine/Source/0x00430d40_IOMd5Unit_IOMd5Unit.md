---
offset: "0x00430d40"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/iounit/IOChecksumUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00430d40 — `IOMd5Unit_IOMd5Unit`

- **Адрес (Offset):** `0x00430d40`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/iounit/IOChecksumUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00430d40
IOMd5Unit::IOMd5Unit(int64_t size, Callback callback, bool readToEnd, IOChecksumUnit** self, bool ownsMemory, IOUnit* next) : IOChecksumUnit(size, readToEnd, self, ownsMemory, next) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00430d40 в IDA Pro / Ghidra
