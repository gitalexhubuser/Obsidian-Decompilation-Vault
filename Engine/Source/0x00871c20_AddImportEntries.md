---
offset: "0x00871c20"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsVersionHash.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00871c20 — `AddImportEntries`

- **Адрес (Offset):** `0x00871c20`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsVersionHash.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00871c20
static int32_t AddImportEntries(OsVersionHash& hash, const uint8_t* image, const IMAGE_IMPORT_DESCRIPTOR* imports, uint32_t importAddress, uint32_t importSize, int32_t unrelocate, bool is32Bit) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00871c20 в IDA Pro / Ghidra
