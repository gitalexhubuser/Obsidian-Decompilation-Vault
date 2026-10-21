---
offset: "0x006afce0"
module: "Engine/Source"
file: "Engine/Source/BLPFile/blp.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x006afce0 — `CBLPFile_Lock2`

- **Адрес (Offset):** `0x006afce0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BLPFile/blp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006afce0
int32_t CBLPFile::Lock2(const char* fileName, PIXEL_FORMAT format, uint32_t mipLevel, uint8_t* data, uint32_t& stride) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006afce0 в IDA Pro / Ghidra
