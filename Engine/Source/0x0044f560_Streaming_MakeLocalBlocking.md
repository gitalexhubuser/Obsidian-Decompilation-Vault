---
offset: "0x0044f560"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Streaming.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0044f560 — `Streaming_MakeLocalBlocking`

- **Адрес (Offset):** `0x0044f560`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Streaming.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0044f560
bool Blizzard::Streaming::MakeLocalBlocking(Blizzard::File::StreamRecord* file, int64_t offset, int32_t size, int32_t priority, const char* name) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0044f560 в IDA Pro / Ghidra
