---
offset: "0x008a1770"
module: "WoW/Source"
file: "WoW/Source/LiquidSystem/Liquid.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008a1770 — `Liquid_Initialize`

- **Адрес (Offset):** `0x008a1770`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/LiquidSystem/Liquid.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008a1770
int32_t Liquid::Initialize(int32_t useCameraRelativeCoords, float worldCoordScale, int32_t shadersEnabled, const char* shaderPath, IDatabase<LiquidTypeRec>* liquidTypeDB, IDatabase<LiquidMaterialRec>* liquidMaterialDB) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008a1770 в IDA Pro / Ghidra
