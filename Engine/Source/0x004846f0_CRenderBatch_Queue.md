---
offset: "0x004846f0"
module: "Engine/Source"
file: "Engine/Source/Frame/CRenderBatch.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004846f0 — `CRenderBatch_Queue`

- **Адрес (Offset):** `0x004846f0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Frame/CRenderBatch.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004846f0
void CRenderBatch::Queue(CTexture* texture, EGxBlend alphaMode, int32_t posCount, const C3Vector* position, const C2Vector* texCoord, int32_t colorCount, const CImVector* color, int32_t idxCount, const uint16_t* indices, CGxShader* shader) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004846f0 в IDA Pro / Ghidra
