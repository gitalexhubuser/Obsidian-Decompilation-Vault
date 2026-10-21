---
offset: "0x00454870"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/File/Win64/Filestack.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00454870 — `System_File_read_overlapped`

- **Адрес (Offset):** `0x00454870`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/File/Win64/Filestack.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00454870
bool System_File::read_overlapped(Blizzard::File::StreamRecord* file, void* buffer, OVERLAPPED* overlapped, int32_t* count) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00454870 в IDA Pro / Ghidra
