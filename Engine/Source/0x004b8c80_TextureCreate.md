---
offset: "0x004b8c80"
module: "Engine/Source"
file: "Engine/Source/Services/Texture.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004b8c80 — `TextureCreate`

- **Адрес (Offset):** `0x004b8c80`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Services/Texture.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004b8c80
CTexture* TextureCreate(EGxTexTarget target, uint32_t width, uint32_t height, uint32_t depth, EGxTexFormat format, EGxTexFormat dataFormat, CGxTexFlags texFlags, void* userArg, GxTexUserFunc userFunc, const char* name, int32_t defaultFilter) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004b8c80 в IDA Pro / Ghidra
