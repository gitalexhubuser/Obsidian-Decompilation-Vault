---
offset: "0x0045f7d0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0045f7d0 — `FindFileInOneArchive`

- **Адрес (Offset):** `0x0045f7d0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0045f7d0
int32_t FindFileInOneArchive(System_SFile::ARCHIVEREC* archive, const char* name, const uint64_t& hash, const Blizzard::Util::Digest<16>& md5, uint32_t flags, System_SFile::FileLookup* lookup) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0045f7d0 в IDA Pro / Ghidra
