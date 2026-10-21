---
offset: "0x004269a0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SComp.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004269a0 — `System_SComp_Bzip2Compress`

- **Адрес (Offset):** `0x004269a0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SComp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004269a0
void System_SComp::Bzip2Compress(void* dest, uint32_t* destSize, const void* source, uint32_t sourceSize, uint32_t* hint, uint8_t level) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004269a0 в IDA Pro / Ghidra
