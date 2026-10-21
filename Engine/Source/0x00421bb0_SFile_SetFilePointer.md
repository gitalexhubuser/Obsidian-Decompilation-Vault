---
offset: "0x00421bb0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/SFile2-Core.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00421bb0 — `SFile_SetFilePointer`

- **Адрес (Offset):** `0x00421bb0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/SFile2-Core.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00421bb0
int32_t STORMAPI SFile::SetFilePointer(SFileImpl* file, int32_t distance, int32_t* distanceHigh, uint32_t method) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00421bb0 в IDA Pro / Ghidra
