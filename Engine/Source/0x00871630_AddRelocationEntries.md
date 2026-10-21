---
offset: "0x00871630"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsVersionHash.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00871630 — `AddRelocationEntries`

- **Адрес (Offset):** `0x00871630`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsVersionHash.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00871630
static int32_t AddRelocationEntries(OsVersionHash& hash, const uint8_t* image, uint64_t imageBase, const IMAGE_DATA_DIRECTORY* directory, int32_t unrelocate, bool is32Bit) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00871630 в IDA Pro / Ghidra
