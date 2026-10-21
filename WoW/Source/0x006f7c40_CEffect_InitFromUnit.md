---
offset: "0x006f7c40"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Effect_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006f7c40 — `CEffect_InitFromUnit`

- **Адрес (Offset):** `0x006f7c40`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Effect_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006f7c40
void CEffect::InitFromUnit(C3Vector position, uint32_t time, int32_t spellId, const SpellVisualKitRec* kit, const SpellVisualEffectNameRec* effectName, const WOWGUID* guid, uint32_t flags, void (*callback)(CM2Model*, uint32_t, uint32_t, int32_t, uint32_t, uint64_t), uint32_t a9, const SpellVisualKitModelAttachRec* attach, WOWGUID transport) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006f7c40 в IDA Pro / Ghidra
