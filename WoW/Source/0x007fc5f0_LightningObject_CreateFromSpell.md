---
offset: "0x007fc5f0"
module: "WoW/Source"
file: "WoW/Source/Magic/MagicClient/SpellVisuals.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007fc5f0 — `LightningObject_CreateFromSpell`

- **Адрес (Offset):** `0x007fc5f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Magic/MagicClient/SpellVisuals.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007fc5f0
void LightningObject::CreateFromSpell(CGObject_C* caster, CEffect* effect, uint32_t chainEffectsId, const WOWGUID* targets, uint32_t count, uint32_t spellId, bool persist, bool reverse, LightningObject** lightning, uint32_t maxLightning, const C3Vector* location, int32_t attachment) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007fc5f0 в IDA Pro / Ghidra
