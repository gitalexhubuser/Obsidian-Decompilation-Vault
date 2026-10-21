---
offset: "0x00427660"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/File/File.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00427660 — `File_ProcessDirFast`

- **Адрес (Offset):** `0x00427660`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/File/File.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00427660
bool Blizzard::File::ProcessDirFast(const char* path, void* cookie, ProcessDirCallback callback, bool treatSymlinksAsFiles) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00427660 в IDA Pro / Ghidra
