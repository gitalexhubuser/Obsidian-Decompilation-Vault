---
offset: "0x004e8660"
module: "WoW/Common"
file: "WoW/Common/ComponentCore/CharacterComponent.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_common
---

# 0x004e8660 — `CCharacterComponent_PasteTransparent4Bit`

- **Адрес (Offset):** `0x004e8660`
- **Модуль:** `WoW/Common`
- **Файл исходника:** `WoW/Common/ComponentCore/CharacterComponent.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004e8660
void CCharacterComponent::PasteTransparent4Bit(void* texture, const BlpPalPixel* pal, MipBits* dstMips, C2iVector& dstPos, uint32_t dstStride, C2iVector& srcPos, C2iVector& srcSize, TCTEXTUREINFO& srcInfo, uint32_t srcMipLevel, int32_t dstMipOffset) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004e8660 в IDA Pro / Ghidra
