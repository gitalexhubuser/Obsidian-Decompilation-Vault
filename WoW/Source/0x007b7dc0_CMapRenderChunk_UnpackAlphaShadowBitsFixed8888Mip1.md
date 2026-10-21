---
offset: "0x007b7dc0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapRenderChunk.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007b7dc0 — `CMapRenderChunk_UnpackAlphaShadowBitsFixed8888Mip1`

- **Адрес (Offset):** `0x007b7dc0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapRenderChunk.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007b7dc0
void __stdcall CMapRenderChunk::UnpackAlphaShadowBitsFixed8888Mip1(CImVector* dstBase, int32_t dstOffset, int32_t dstPitch, uint32_t size, SLayerAlpha* cursors, int32_t alphaSlot, uint8_t* shadowMap) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007b7dc0 в IDA Pro / Ghidra
