---
offset: "0x0045c880"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0045c880 — `System_SFile_FindBlockEntry`

- **Адрес (Offset):** `0x0045c880`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0045c880
uint32_t System_SFile::FindBlockEntry(ARCHIVEREC* archive, const Blizzard::Util::Digest<16>& md5, bool* deleted) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0045c880 в IDA Pro / Ghidra
