---
offset: "0x0044ed80"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Storage.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0044ed80 — `Storage_Acquire`

- **Адрес (Offset):** `0x0044ed80`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Storage.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0044ed80
Blizzard::Streaming::StorageEntry* Blizzard::Storage::Acquire(Blizzard::File::Filesystem* fs, const std::string& key, const char* path, int64_t size, const char* version, int32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0044ed80 в IDA Pro / Ghidra
