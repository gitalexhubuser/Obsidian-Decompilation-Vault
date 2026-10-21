---
offset: "0x004b6760"
module: "Engine/Source"
file: "Engine/Source/Services/Texture.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004b6760 — `TextureAllocGxTex`

- **Адрес (Offset):** `0x004b6760`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Services/Texture.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004b6760
CGxTex* TextureAllocGxTex(EGxTexTarget target, uint32_t width, uint32_t height, uint32_t depth, EGxTexFormat format, CGxTexFlags flags, void* userArg, GxTexUserFunc userFunc, EGxTexFormat dataFormat, const char* name) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004b6760 в IDA Pro / Ghidra
