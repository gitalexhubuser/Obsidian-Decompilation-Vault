---
offset: "0x00779fb0"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/IOFileUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00779fb0 — `IOUnbufferedFileUnit_Read`

- **Адрес (Offset):** `0x00779fb0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/IOFileUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00779fb0
bool IOUnbufferedFileUnit::Read(void* buffer, int64_t offset, uint32_t count, uint32_t* bytesRead) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00779fb0 в IDA Pro / Ghidra
