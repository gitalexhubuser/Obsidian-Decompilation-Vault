---
offset: "0x0077f4c0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0077f4c0 — `UpdateShadowGxTex`

- **Адрес (Offset):** `0x0077f4c0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077f4c0
static void UpdateShadowGxTex(EGxTexCommand command, uint32_t width, uint32_t height, uint32_t face, uint32_t level, void* userArg, uint32_t& texelStrideInBytes, const void*& texels) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077f4c0 в IDA Pro / Ghidra
