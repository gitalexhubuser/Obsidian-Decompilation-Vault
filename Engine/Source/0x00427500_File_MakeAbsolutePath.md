---
offset: "0x00427500"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/File/File.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00427500 — `File_MakeAbsolutePath`

- **Адрес (Offset):** `0x00427500`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/File/File.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00427500
bool Blizzard::File::MakeAbsolutePath(const char* rel, char* result, int32_t resultsize, bool canonicalize) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00427500 в IDA Pro / Ghidra
