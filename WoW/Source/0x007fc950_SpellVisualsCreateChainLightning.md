---
offset: "0x007fc950"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/SpellVisuals.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007fc950 — `SpellVisualsCreateChainLightning`

- **Адрес (Offset):** `0x007fc950`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/SpellVisuals.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007fc950
void SpellVisualsCreateChainLightning(CGUnit_C* caster, CEffect* effect, uint32_t chainEffectsId, bool persist, bool reverse, uint32_t spellId, const WOWGUID* targets, uint32_t count, LightningObject** lightning, uint32_t maxLightning, const C3Vector* location, int32_t attachment) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007fc950 в IDA Pro / Ghidra
