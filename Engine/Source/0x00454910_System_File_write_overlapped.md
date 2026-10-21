---
offset: "0x00454910"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/File/Win64/Filestack.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00454910 — `System_File_write_overlapped`

- **Адрес (Offset):** `0x00454910`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/File/Win64/Filestack.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00454910
bool System_File::write_overlapped(Blizzard::File::StreamRecord* file, void* buffer, OVERLAPPED* overlapped, int32_t* count) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00454910 в IDA Pro / Ghidra
