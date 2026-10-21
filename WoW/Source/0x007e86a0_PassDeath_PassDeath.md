---
offset: "0x007e86a0"
module: "WoW/Source"
file: "WoW/Source/Game/GameClient/FFXEffects.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007e86a0 — `PassDeath_PassDeath`

- **Адрес (Offset):** `0x007e86a0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Game/GameClient/FFXEffects.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007e86a0
PassDeath::PassDeath(FFX::Tex** inputs, uint32_t count, FFX::Tex* output, EGxBlend blend, bool unk) : FFX::Pass(inputs, count, output, blend, unk) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007e86a0 в IDA Pro / Ghidra
