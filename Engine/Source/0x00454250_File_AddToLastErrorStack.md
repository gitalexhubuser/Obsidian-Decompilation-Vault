---
offset: "0x00454250"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/File/File.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00454250 — `File_AddToLastErrorStack`

- **Адрес (Offset):** `0x00454250`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/File/File.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00454250
void Blizzard::File::AddToLastErrorStack(int32_t errCode, const char* errStr, int32_t category) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00454250 в IDA Pro / Ghidra
