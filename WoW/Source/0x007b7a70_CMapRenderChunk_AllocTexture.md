---
offset: "0x007b7a70"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapRenderChunk.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007b7a70 — `CMapRenderChunk_AllocTexture`

- **Адрес (Offset):** `0x007b7a70`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapRenderChunk.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007b7a70
CTexture* CMapRenderChunk::AllocTexture(uint32_t width, uint32_t height, void* userArg, GxTexUserFunc userFunc, EGxTexFormat format, EGxTexFormat dataFormat) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007b7a70 в IDA Pro / Ghidra
