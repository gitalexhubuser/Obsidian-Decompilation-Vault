---
offset: "0x004549b0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/File/Win64/Filestack.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004549b0 — `System_File_ToCreateFlags`

- **Адрес (Offset):** `0x004549b0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/File/Win64/Filestack.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004549b0
bool System_File::ToCreateFlags(uint32_t flags, DWORD* sharemode, DWORD* desiredaccess, DWORD* creationdisposition, DWORD* flagsandattributes) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004549b0 в IDA Pro / Ghidra
