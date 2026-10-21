---
offset: "0x006c74d0"
module: "Engine/Source"
file: "Engine/Source/Gxu/GxuFontString.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x006c74d0 — `CGxString_Initialize`

- **Адрес (Offset):** `0x006c74d0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Gxu/GxuFontString.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006c74d0
int32_t CGxString::Initialize(float fontHeight, const C3Vector& position, float blockWidth, float blockHeight, CGxFont* face, const char* text, EGxFontVJusts vertJust, EGxFontHJusts horzJust, float spacing, uint32_t flags, const CImVector& color, float scale) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006c74d0 в IDA Pro / Ghidra
