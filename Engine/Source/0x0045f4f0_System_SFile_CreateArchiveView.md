---
offset: "0x0045f4f0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0045f4f0 — `System_SFile_CreateArchiveView`

- **Адрес (Offset):** `0x0045f4f0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0045f4f0
bool System_SFile::CreateArchiveView(IOUnit* file, const char* name, int32_t priority, uint32_t userDataSize, ARCHIVEREC** result, const Blizzard::Mopaq::ArchiveOptions* options) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0045f4f0 в IDA Pro / Ghidra
