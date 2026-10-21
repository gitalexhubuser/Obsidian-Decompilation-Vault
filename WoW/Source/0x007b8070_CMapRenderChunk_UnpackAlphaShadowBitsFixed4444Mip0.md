---
offset: "0x007b8070"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapRenderChunk.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007b8070 — `CMapRenderChunk_UnpackAlphaShadowBitsFixed4444Mip0`

- **Адрес (Offset):** `0x007b8070`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapRenderChunk.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007b8070
void __stdcall CMapRenderChunk::UnpackAlphaShadowBitsFixed4444Mip0(uint16_t* dstBase, int32_t dstOffset, int32_t dstPitch, uint32_t size, SLayerAlpha* cursors, uint8_t* shadowMap) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007b8070 в IDA Pro / Ghidra
