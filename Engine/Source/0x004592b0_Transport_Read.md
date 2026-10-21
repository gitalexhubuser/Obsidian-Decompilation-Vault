---
offset: "0x004592b0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Transport.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004592b0 — `Transport_Read`

- **Адрес (Offset):** `0x004592b0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Transport.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004592b0
bool Blizzard::Streaming::Transport::Read(Manifests::TransportItem* transport, std::string url, int32_t maxRetry, void* data, int64_t fileSize, int64_t offset, int32_t size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004592b0 в IDA Pro / Ghidra
