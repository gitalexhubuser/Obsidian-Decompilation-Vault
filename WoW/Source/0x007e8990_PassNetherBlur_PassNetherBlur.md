---
offset: "0x007e8990"
module: "WoW/Source"
file: "WoW/Source/Game/GameClient/FFXEffects.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007e8990 — `PassNetherBlur_PassNetherBlur`

- **Адрес (Offset):** `0x007e8990`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Game/GameClient/FFXEffects.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007e8990
PassNetherBlur::PassNetherBlur(FFX::Tex** inputs, uint32_t count, FFX::Tex* output, EGxBlend blend, bool unk) : FFX::Pass(inputs, count, output, blend, unk) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007e8990 в IDA Pro / Ghidra
