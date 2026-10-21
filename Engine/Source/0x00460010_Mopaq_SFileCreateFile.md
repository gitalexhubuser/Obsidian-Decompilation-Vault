---
offset: "0x00460010"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00460010 — `Mopaq_SFileCreateFile`

- **Адрес (Offset):** `0x00460010`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00460010
bool Blizzard::Mopaq::SFileCreateFile(System_SFile::ARCHIVEREC* handle, const char* name, uint32_t size, uint32_t flags, IOMpqUnit** result) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00460010 в IDA Pro / Ghidra
