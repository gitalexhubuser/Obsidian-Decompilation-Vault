---
offset: "0x006be2b0"
module: "Engine/Source"
file: "Engine/Source/Gxu/GxuFontMain.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x006be2b0 — `GxuFontCreateString`

- **Адрес (Offset):** `0x006be2b0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Gxu/GxuFontMain.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006be2b0
int32_t GxuFontCreateString(CGxFont* face, const char* text, float fontHeight, const C3Vector& position, float blockWidth, float blockHeight, float spacing, CGxString*& string, EGxFontVJusts vertJust, EGxFontHJusts horzJust, uint32_t flags, const CImVector& color, float unused, float scale) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006be2b0 в IDA Pro / Ghidra
