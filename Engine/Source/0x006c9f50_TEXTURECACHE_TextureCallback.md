---
offset: "0x006c9f50"
module: "Engine/Source"
file: "Engine/Source/Gxu/GxuFontTextureCache.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x006c9f50 — `TEXTURECACHE_TextureCallback`

- **Адрес (Offset):** `0x006c9f50`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Gxu/GxuFontTextureCache.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006c9f50
void TEXTURECACHE::TextureCallback(EGxTexCommand command, uint32_t width, uint32_t height, uint32_t face, uint32_t level, void* userArg, uint32_t& texelStrideInBytes, const void*& texels) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006c9f50 в IDA Pro / Ghidra
