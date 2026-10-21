---
offset: "0x00681d90"
module: "Engine/Source"
file: "Engine/Source/Gx/Gx.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00681d90 — `GxTexCreate`

- **Адрес (Offset):** `0x00681d90`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Gx/Gx.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00681d90
int32_t GxTexCreate(EGxTexTarget target, uint32_t width, uint32_t height, uint32_t depth, EGxTexFormat format, EGxTexFormat dataFormat, CGxTexFlags flags, void* userArg, GxTexUserFunc userFunc, const char* name, CGxTex*& texId) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00681d90 в IDA Pro / Ghidra
