---
offset: "0x00871d20"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsVersionHash.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00871d20 — `ComputeChecksum`

- **Адрес (Offset):** `0x00871d20`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsVersionHash.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00871d20
static int32_t ComputeChecksum(IOsVersionHashCallback& callback, const uint8_t* image, int32_t unrelocate) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00871d20 в IDA Pro / Ghidra
