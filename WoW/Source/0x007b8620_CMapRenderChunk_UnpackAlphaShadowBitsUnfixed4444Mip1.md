---
offset: "0x007b8620"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapRenderChunk.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007b8620 — `CMapRenderChunk_UnpackAlphaShadowBitsUnfixed4444Mip1`

- **Адрес (Offset):** `0x007b8620`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapRenderChunk.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007b8620
void __stdcall CMapRenderChunk::UnpackAlphaShadowBitsUnfixed4444Mip1(uint16_t* dstBase, int32_t dstOffset, int32_t dstPitch, uint32_t size, SLayerAlpha* cursors, uint8_t* shadowMap) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007b8620 в IDA Pro / Ghidra
