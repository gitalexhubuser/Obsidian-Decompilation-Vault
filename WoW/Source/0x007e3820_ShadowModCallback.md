---
offset: "0x007e3820"
module: "WoW/Source"
file: "WoW/Source/WorldClient/shadow.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007e3820 — `ShadowModCallback`

- **Адрес (Offset):** `0x007e3820`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/shadow.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007e3820
static void ShadowModCallback(EGxTexCommand command, uint32_t width, uint32_t height, uint32_t depth, uint32_t mipLevel, void* userArg, uint32_t& texelStrideInBytes, const void*& texels) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007e3820 в IDA Pro / Ghidra
