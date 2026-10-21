---
offset: "0x00431380"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SComp.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00431380 — `System_SComp_DecompressBlock`

- **Адрес (Offset):** `0x00431380`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SComp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00431380
bool __stdcall System_SComp::DecompressBlock(void* dst, uint32_t* dstSize, const void* src, uint32_t srcSize, Decompressor* decompressors) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00431380 в IDA Pro / Ghidra
