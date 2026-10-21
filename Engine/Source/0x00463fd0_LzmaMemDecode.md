---
offset: "0x00463fd0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SComp.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00463fd0 — `LzmaMemDecode`

- **Адрес (Offset):** `0x00463fd0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SComp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00463fd0
bool LzmaMemDecode(const uint8_t* source, uint32_t sourceSize, uint8_t* dest, uint32_t destSize, uint32_t* destProcessed, void* (*alloc)(uint32_t size), void (*free)(void* address)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00463fd0 в IDA Pro / Ghidra
