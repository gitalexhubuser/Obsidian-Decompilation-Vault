---
offset: "0x007b7c60"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapRenderChunk.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007b7c60 — `CMapRenderChunk_UnpackAlphaShadowBitsFixed8888Mip0`

- **Адрес (Offset):** `0x007b7c60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapRenderChunk.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007b7c60
void __stdcall CMapRenderChunk::UnpackAlphaShadowBitsFixed8888Mip0(CImVector* dstBase, int32_t dstOffset, int32_t dstPitch, uint32_t size, SLayerAlpha* cursors, int32_t alphaSlot, uint8_t* shadowMap) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007b7c60 в IDA Pro / Ghidra
