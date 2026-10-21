---
offset: "0x00462000"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsFile.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00462000 — `OsFileList`

- **Адрес (Offset):** `0x00462000`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsFile.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00462000
int32_t OsFileList(const char* dir, const char* pattern, OsFileListCallback callback, void* param, int32_t includeHidden) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00462000 в IDA Pro / Ghidra
