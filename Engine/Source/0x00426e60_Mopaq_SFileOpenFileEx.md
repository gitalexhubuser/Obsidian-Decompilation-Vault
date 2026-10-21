---
offset: "0x00426e60"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFile.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00426e60 — `Mopaq_SFileOpenFileEx`

- **Адрес (Offset):** `0x00426e60`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFile.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00426e60
int32_t Blizzard::Mopaq::SFileOpenFileEx(System_SFile::ARCHIVEREC* handle, const char* name, uint32_t flags, IOMpqUnit** result) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00426e60 в IDA Pro / Ghidra
