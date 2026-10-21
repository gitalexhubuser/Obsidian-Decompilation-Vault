---
offset: "0x00871790"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsVersionHash.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00871790 — `HashEntry`

- **Адрес (Offset):** `0x00871790`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsVersionHash.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00871790
static int32_t HashEntry(IOsVersionHashCallback& callback, const OsVersionHashEntry& entry, const uint8_t* image, uint64_t imageBase, const uint8_t* data, int32_t unrelocate, bool is32Bit) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00871790 в IDA Pro / Ghidra
