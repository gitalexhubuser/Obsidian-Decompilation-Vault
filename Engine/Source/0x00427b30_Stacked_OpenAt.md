---
offset: "0x00427b30"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/File/Filestack_Streaming.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00427b30 — `Stacked_OpenAt`

- **Адрес (Offset):** `0x00427b30`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/File/Filestack_Streaming.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00427b30
Blizzard::File::StreamRecord* STORMAPI System_File::Stacked::OpenAt(Blizzard::File::Filesystem* fs, Blizzard::File::StreamRecord* file, const char* path, int32_t mode) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00427b30 в IDA Pro / Ghidra
