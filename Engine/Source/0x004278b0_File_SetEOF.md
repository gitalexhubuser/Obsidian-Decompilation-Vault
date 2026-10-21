---
offset: "0x004278b0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/File/File.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004278b0 — `File_SetEOF`

- **Адрес (Offset):** `0x004278b0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/File/File.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004278b0
bool Blizzard::File::SetEOF(StreamRecord* file, int64_t offset, int32_t whence) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004278b0 в IDA Pro / Ghidra
