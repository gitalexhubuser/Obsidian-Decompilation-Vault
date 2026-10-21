---
offset: "0x007b87f0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapRenderChunk.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007b87f0 — `CMapRenderChunk_UnpackAlphaShadowBits`

- **Адрес (Offset):** `0x007b87f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapRenderChunk.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007b87f0
void CMapRenderChunk::UnpackAlphaShadowBits(void* dstBase, int32_t dstOffset, int32_t dstPitch, uint32_t size, SLayerAlpha* cursors, int32_t alphaSlot, uint8_t* shadowMap, int32_t genFormat, int32_t doNotFixAlphaMap) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007b87f0 в IDA Pro / Ghidra
