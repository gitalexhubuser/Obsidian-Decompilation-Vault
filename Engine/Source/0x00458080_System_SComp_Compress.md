---
offset: "0x00458080"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SComp.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00458080 — `System_SComp_Compress`

- **Адрес (Offset):** `0x00458080`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SComp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00458080
bool System_SComp::Compress(void* dst, uint32_t* dstSize, bool* checksum, const void* src, uint32_t srcSize, uint32_t count, const Blizzard::Mopaq::CompressionAlgorithm* algorithms) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00458080 в IDA Pro / Ghidra
