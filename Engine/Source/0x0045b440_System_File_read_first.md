---
offset: "0x0045b440"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/File/Win64/Filestack.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0045b440 — `System_File_read_first`

- **Адрес (Offset):** `0x0045b440`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/File/Win64/Filestack.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0045b440
bool System_File::read_first(Blizzard::File::StreamRecord* file, void* buffer, OVERLAPPED* overlapped, int32_t* count) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0045b440 в IDA Pro / Ghidra
