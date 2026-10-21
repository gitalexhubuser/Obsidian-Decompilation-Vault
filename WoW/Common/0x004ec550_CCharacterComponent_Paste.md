---
offset: "0x004ec550"
module: "WoW/Common"
file: "WoW/Common/ComponentCore/CharacterComponent.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_common
---

# 0x004ec550 — `CCharacterComponent_Paste`

- **Адрес (Offset):** `0x004ec550`
- **Модуль:** `WoW/Common`
- **Файл исходника:** `WoW/Common/ComponentCore/CharacterComponent.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004ec550
void CCharacterComponent::Paste(void* texture, MipBits* dstMips, const C2iVector& dstPos, const C2iVector& srcPos, const C2iVector& srcSize, TCTEXTUREINFO& srcInfo, uint32_t srcMipLevel) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004ec550 в IDA Pro / Ghidra
