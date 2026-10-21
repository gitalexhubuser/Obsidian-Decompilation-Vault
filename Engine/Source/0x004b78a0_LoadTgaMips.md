---
offset: "0x004b78a0"
module: "Engine/Source"
file: "Engine/Source/Services/Texture.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004b78a0 — `LoadTgaMips`

- **Адрес (Offset):** `0x004b78a0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Services/Texture.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004b78a0
int32_t LoadTgaMips(char* fileName, char* extension, int32_t flags, MipBits** images, uint32_t* width, uint32_t* height, EGxTexFormat* gxTexFormat, int32_t* opaque, uint32_t* alphaBits, PIXEL_FORMAT* pixelFormat) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004b78a0 в IDA Pro / Ghidra
