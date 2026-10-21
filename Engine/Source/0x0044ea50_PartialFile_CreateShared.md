---
offset: "0x0044ea50"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Storage.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0044ea50 — `PartialFile_CreateShared`

- **Адрес (Offset):** `0x0044ea50`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Storage.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0044ea50
Blizzard::Streaming::StorageEntry* Blizzard::Storage::PartialFile::CreateShared(const std::string& key, const char* path, int64_t size, const char* version, int32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0044ea50 в IDA Pro / Ghidra
