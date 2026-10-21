---
offset: "0x004be040"
module: "Engine/Source"
file: "Engine/Source/Services/TextBlock.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004be040 — `TextBlockWrapText`

- **Адрес (Offset):** `0x004be040`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Services/TextBlock.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004be040
uint32_t TextBlockWrapText(HTEXTFONT font, const char* text, float fontHeight, float blockWidth, uint32_t* lineStarts, uint32_t maxLines, float shadowWidth, float scale, float unused, uint32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004be040 в IDA Pro / Ghidra
