---
offset: "0x00444550"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Streaming.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00444550 — `Streaming_QueueLoad`

- **Адрес (Offset):** `0x00444550`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Streaming.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00444550
bool Blizzard::Streaming::QueueLoad(Blizzard::File::StreamRecord* file, int32_t priority, LoadRange* range, Completion* completion) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00444550 в IDA Pro / Ghidra
