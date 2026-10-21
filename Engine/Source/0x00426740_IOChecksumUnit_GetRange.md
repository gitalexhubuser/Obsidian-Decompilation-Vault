---
offset: "0x00426740"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/iounit/IOChecksumUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00426740 — `IOChecksumUnit_GetRange`

- **Адрес (Offset):** `0x00426740`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/iounit/IOChecksumUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00426740
bool IOChecksumUnit::GetRange(const uint8_t* data, int64_t offset, uint32_t count, const uint8_t** rangeData, uint32_t* rangeCount) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00426740 в IDA Pro / Ghidra
