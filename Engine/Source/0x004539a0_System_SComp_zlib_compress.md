---
offset: "0x004539a0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SComp.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004539a0 — `System_SComp_zlib_compress`

- **Адрес (Offset):** `0x004539a0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SComp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004539a0
int System_SComp::zlib_compress(uint8_t* dest, uint32_t* destLen, const uint8_t* source, uint32_t sourceLen, int level) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004539a0 в IDA Pro / Ghidra
