---
offset: "0x006f7d60"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Effect_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006f7d60 — `CEffect_InitAtPosition`

- **Адрес (Offset):** `0x006f7d60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Effect_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006f7d60
void CEffect::InitAtPosition(int32_t spellId, const SpellVisualKitRec* kit, const SpellVisualEffectNameRec* effectName, uint32_t flags, void (*callback)(CM2Model*, uint32_t, uint32_t, int32_t, uint32_t, uint64_t), const C3Vector* position, uint32_t a8, WOWGUID transport) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006f7d60 в IDA Pro / Ghidra
