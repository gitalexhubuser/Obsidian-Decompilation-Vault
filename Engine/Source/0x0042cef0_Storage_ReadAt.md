---
offset: "0x0042cef0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Storage.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0042cef0 — `Storage_ReadAt`

- **Адрес (Offset):** `0x0042cef0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Storage.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0042cef0
bool Blizzard::Storage::ReadAt(Blizzard::File::Filesystem* fs, Blizzard::File::StreamRecord* file, void* buffer, int64_t offset, int32_t size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0042cef0 в IDA Pro / Ghidra
