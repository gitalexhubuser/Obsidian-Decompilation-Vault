---
offset: "0x004443e0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Storage.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004443e0 — `Storage_QueueWrite`

- **Адрес (Offset):** `0x004443e0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Storage.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004443e0
bool Blizzard::Storage::QueueWrite(Blizzard::File::Filesystem* fs, Blizzard::File::StreamRecord* file, uint8_t* data, int64_t offset, int32_t size, bool owned) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004443e0 в IDA Pro / Ghidra
