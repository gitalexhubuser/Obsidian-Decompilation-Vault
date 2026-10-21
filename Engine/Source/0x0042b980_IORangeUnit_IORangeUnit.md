---
offset: "0x0042b980"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/iounit/IOUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0042b980 — `IORangeUnit_IORangeUnit`

- **Адрес (Offset):** `0x0042b980`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/iounit/IOUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0042b980
IORangeUnit::IORangeUnit(int64_t start, int64_t end, bool ownsMemory, IOUnit* next) : IOUnit(next, ownsMemory) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0042b980 в IDA Pro / Ghidra
