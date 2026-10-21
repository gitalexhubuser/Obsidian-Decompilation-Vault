---
offset: "0x0044f120"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Streaming.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0044f120 — `Streaming_CheckFileRange`

- **Адрес (Offset):** `0x0044f120`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Streaming.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0044f120
int32_t Blizzard::Streaming::CheckFileRange(const char* path, int64_t offset, int32_t size, const char* name, int32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0044f120 в IDA Pro / Ghidra
