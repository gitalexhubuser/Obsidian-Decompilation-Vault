---
offset: "0x00453b20"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SComp.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00453b20 — `System_SComp_zlib_decompress`

- **Адрес (Offset):** `0x00453b20`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SComp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00453b20
int System_SComp::zlib_decompress(uint8_t* dest, uint32_t* destLen, const uint8_t* source, uint32_t sourceLen) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00453b20 в IDA Pro / Ghidra
