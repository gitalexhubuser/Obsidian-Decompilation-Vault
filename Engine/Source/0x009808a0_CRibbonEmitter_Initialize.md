---
offset: "0x009808a0"
module: "Engine/Source"
file: "Engine/Source/Services/RibbonEmitter.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x009808a0 — `CRibbonEmitter_Initialize`

- **Адрес (Offset):** `0x009808a0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Services/RibbonEmitter.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009808a0
void CRibbonEmitter::Initialize(float edgesPerSecond, float edgeLifetime, const CImVector& color, const TSGrowableArray<CTexture*>& textures, const TSGrowableArray<CRibbonMat>& materials, const TSGrowableArray<uint32_t>& textureTypes, const CAaRect& texCoords, uint32_t rows, uint32_t cols) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x009808a0 в IDA Pro / Ghidra
