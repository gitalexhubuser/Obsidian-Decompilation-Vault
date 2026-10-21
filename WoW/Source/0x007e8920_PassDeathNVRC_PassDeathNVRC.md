---
offset: "0x007e8920"
module: "WoW/Source"
file: "WoW/Source/Game/GameClient/FFXEffects.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007e8920 — `PassDeathNVRC_PassDeathNVRC`

- **Адрес (Offset):** `0x007e8920`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Game/GameClient/FFXEffects.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007e8920
PassDeathNVRC::PassDeathNVRC(FFX::Tex** inputs, uint32_t count, FFX::Tex* output, EGxBlend blend, bool unk) : FFX::Pass(inputs, count, output, blend, unk) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007e8920 в IDA Pro / Ghidra
