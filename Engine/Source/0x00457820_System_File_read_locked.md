---
offset: "0x00457820"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/File/Win64/Filestack.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00457820 — `System_File_read_locked`

- **Адрес (Offset):** `0x00457820`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/File/Win64/Filestack.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00457820
bool System_File::read_locked(Blizzard::File::StreamRecord* file, void* buffer, OVERLAPPED* overlapped, int32_t* count) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00457820 в IDA Pro / Ghidra
