---
offset: "0x00871980"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsVersionHash.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00871980 — `HashSection`

- **Адрес (Offset):** `0x00871980`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsVersionHash.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00871980
static int32_t HashSection(IOsVersionHashCallback& callback, OsVersionHash& hash, const uint8_t* image, uint64_t imageBase, const IMAGE_SECTION_HEADER* section, uint32_t alignment, int32_t unrelocate, bool is32Bit) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00871980 в IDA Pro / Ghidra
