---
offset: "0x004480b0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Streaming.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004480b0 — `Streaming_MakeLocalAsync`

- **Адрес (Offset):** `0x004480b0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Streaming.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004480b0
bool Blizzard::Streaming::MakeLocalAsync(Blizzard::File::StreamRecord* file, int64_t offset, int32_t size, int32_t priority, const char* name) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004480b0 в IDA Pro / Ghidra
