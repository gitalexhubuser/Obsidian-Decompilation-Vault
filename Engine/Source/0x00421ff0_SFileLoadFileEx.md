---
offset: "0x00421ff0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/SFile2-Core.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00421ff0 — `SFileLoadFileEx`

- **Адрес (Offset):** `0x00421ff0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/SFile2-Core.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00421ff0
int32_t STORMAPI SFileLoadFileEx(SArchive* archive, const char* name, void** data, uint32_t* size, uint32_t extra, uint32_t flags, SOVERLAPPED* overlapped) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00421ff0 в IDA Pro / Ghidra
