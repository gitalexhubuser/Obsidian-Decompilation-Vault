---
offset: "0x004b9200"
module: "Engine/Source"
file: "Engine/Source/Services/Texture.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004b9200 — `TextureCreate`

- **Адрес (Offset):** `0x004b9200`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Services/Texture.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004b9200
CTexture* TextureCreate(uint32_t width, uint32_t height, EGxTexFormat format, EGxTexFormat dataFormat, CGxTexFlags texFlags, void* userArg, GxTexUserFunc userFunc, const char* name, int32_t defaultFilter) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004b9200 в IDA Pro / Ghidra
