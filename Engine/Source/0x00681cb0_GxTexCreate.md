---
offset: "0x00681cb0"
module: "Engine/Source"
file: "Engine/Source/Gx/Gx.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00681cb0 — `GxTexCreate`

- **Адрес (Offset):** `0x00681cb0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Gx/Gx.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00681cb0
int32_t GxTexCreate(uint32_t width, uint32_t height, EGxTexFormat format, CGxTexFlags flags, void* userArg, GxTexUserFunc userFunc, CGxTex*& texId) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00681cb0 в IDA Pro / Ghidra
