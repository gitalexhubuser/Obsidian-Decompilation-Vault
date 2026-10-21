---
offset: "0x00432a40"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Storage.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00432a40 — `Storage_GetRange`

- **Адрес (Offset):** `0x00432a40`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Storage.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00432a40
Blizzard::Streaming::LoadRange* Blizzard::Storage::GetRange(Blizzard::Streaming::StorageEntry* entry, int64_t offset, int32_t size, int32_t* count, bool lock) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00432a40 в IDA Pro / Ghidra
