---
offset: "0x00439c40"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Storage.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00439c40 — `Storage_ReadLocal`

- **Адрес (Offset):** `0x00439c40`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Storage.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00439c40
bool Blizzard::Storage::ReadLocal(Blizzard::File::Filesystem* fs, Blizzard::File::StreamRecord* file, Blizzard::Streaming::StorageEntry* entry, uint8_t* buffer, int64_t offset, int32_t size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00439c40 в IDA Pro / Ghidra
