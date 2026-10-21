---
offset: "0x0042cf20"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Storage.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0042cf20 — `Storage_WriteAt`

- **Адрес (Offset):** `0x0042cf20`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Storage.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0042cf20
bool Blizzard::Storage::WriteAt(Blizzard::File::StreamRecord* file, const void* buffer, int64_t offset, int32_t size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0042cf20 в IDA Pro / Ghidra
