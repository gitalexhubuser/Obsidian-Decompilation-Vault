---
offset: "0x00505930"
module: "WoW/Source"
file: "WoW/Source/Ui/ChatFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00505930 — `CGChat_TranslateMessage`

- **Адрес (Offset):** `0x00505930`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/ChatFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00505930
void CGChat::TranslateMessage(uint32_t language, uint32_t skill, const char* text, char* buffer, uint32_t size, int32_t a6, int32_t a7) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00505930 в IDA Pro / Ghidra
