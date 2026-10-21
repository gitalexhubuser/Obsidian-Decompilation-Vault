---
offset: "0x00581cd0"
module: "WoW/Source"
file: "WoW/Source/Ui/MinimapFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00581cd0 — `CGMinimapFrame_MinimapTextureCallback`

- **Адрес (Offset):** `0x00581cd0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/MinimapFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00581cd0
void CGMinimapFrame::MinimapTextureCallback(EGxTexCommand command, uint32_t width, uint32_t height, uint32_t depth, uint32_t mipLevel, void* userArg, uint32_t& texelStrideInBytes, const void*& texels) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00581cd0 в IDA Pro / Ghidra
