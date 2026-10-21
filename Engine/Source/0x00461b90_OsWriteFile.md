---
offset: "0x00461b90"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsFile.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00461b90 — `OsWriteFile`

- **Адрес (Offset):** `0x00461b90`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsFile.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00461b90
int32_t OsWriteFile(HOSFILE file, const void* buffer, uint32_t bytesToWrite, uint32_t* bytesWritten) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00461b90 в IDA Pro / Ghidra
