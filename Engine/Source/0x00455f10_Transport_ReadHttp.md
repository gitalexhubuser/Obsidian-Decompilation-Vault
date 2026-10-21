---
offset: "0x00455f10"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Transport.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00455f10 — `Transport_ReadHttp`

- **Адрес (Offset):** `0x00455f10`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Transport.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00455f10
bool Blizzard::Streaming::Transport::ReadHttp(Manifests::TransportItem* transport, std::string url, int32_t maxRetry, void* data, int64_t fileSize, int64_t offset, int32_t size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00455f10 в IDA Pro / Ghidra
