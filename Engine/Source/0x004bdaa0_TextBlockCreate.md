---
offset: "0x004bdaa0"
module: "Engine/Source"
file: "Engine/Source/Services/TextBlock.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004bdaa0 — `TextBlockCreate`

- **Адрес (Offset):** `0x004bdaa0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Services/TextBlock.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004bdaa0
HTEXTBLOCK TextBlockCreate(HTEXTFONT font, const char* text, const CImVector& color, const C3Vector& position, float fontHeight, float blockWidth, float blockHeight, uint32_t flags, float charSpacing, float lineSpacing, float scale) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004bdaa0 в IDA Pro / Ghidra
