---
offset: "0x00452320"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Transport.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00452320 — `Transport_GetSplitFileURL`

- **Адрес (Offset):** `0x00452320`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Transport.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00452320
void Blizzard::Streaming::Transport::GetSplitFileURL(const std::string& url, int64_t start, int64_t end, int32_t skip, int32_t splitSize, int32_t md5Size, int32_t size, std::vector<URL_INFO>* urls) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00452320 в IDA Pro / Ghidra
