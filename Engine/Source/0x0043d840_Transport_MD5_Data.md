---
offset: "0x0043d840"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Transport.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0043d840 — `Transport_MD5_Data`

- **Адрес (Offset):** `0x0043d840`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Streaming/Win64/Transport.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0043d840
bool Blizzard::Streaming::Transport::MD5_Data(std::string* out, std::string* data, int32_t md5Size, int64_t start, int64_t end) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0043d840 в IDA Pro / Ghidra
