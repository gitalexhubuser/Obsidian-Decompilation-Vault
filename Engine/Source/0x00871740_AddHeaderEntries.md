---
offset: "0x00871740"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsVersionHash.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00871740 — `AddHeaderEntries`

- **Адрес (Offset):** `0x00871740`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsVersionHash.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00871740
static int32_t AddHeaderEntries(OsVersionHash& hash, const uint8_t* image, uint64_t imageBase, uint32_t sizeOfHeaders, int32_t unrelocate, bool is32Bit) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00871740 в IDA Pro / Ghidra
