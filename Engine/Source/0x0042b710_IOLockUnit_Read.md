---
offset: "0x0042b710"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/iounit/IOUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0042b710 — `IOLockUnit_Read`

- **Адрес (Offset):** `0x0042b710`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/iounit/IOUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0042b710
bool IOLockUnit::Read(void* buffer, int64_t offset, uint32_t count, uint32_t* bytesRead) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0042b710 в IDA Pro / Ghidra
