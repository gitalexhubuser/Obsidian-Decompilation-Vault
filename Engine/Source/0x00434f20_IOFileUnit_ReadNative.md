---
offset: "0x00434f20"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/iounit/Win64/IOFileUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00434f20 — `IOFileUnit_ReadNative`

- **Адрес (Offset):** `0x00434f20`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/iounit/Win64/IOFileUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00434f20
bool IOFileUnit::ReadNative(uint32_t offset, const char* path, void* buffer, uint32_t count, uint32_t* bytesRead) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00434f20 в IDA Pro / Ghidra
