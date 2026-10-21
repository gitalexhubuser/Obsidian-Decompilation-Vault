---
offset: "0x00457d00"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/iounit/IOFileUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00457d00 — `IOUnbufferedFileUnit_Read`

- **Адрес (Offset):** `0x00457d00`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/iounit/IOFileUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00457d00
bool IOUnbufferedFileUnit::Read(void* buffer, int64_t offset, uint32_t count, uint32_t* bytesRead) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00457d00 в IDA Pro / Ghidra
