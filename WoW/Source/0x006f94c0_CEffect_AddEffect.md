---
offset: "0x006f94c0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Effect_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006f94c0 — `CEffect_AddEffect`

- **Адрес (Offset):** `0x006f94c0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Effect_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006f94c0
void CEffect::AddEffect(int32_t attachType, int32_t spellId, const SpellVisualKitRec* kit, const SpellVisualEffectNameRec* effectName, const WOWGUID* target, const WOWGUID* source, uint32_t flags, void (*callback)(CM2Model*, uint32_t, uint32_t, int32_t, uint32_t, uint64_t), const C3Vector* position, uint32_t a10, const SpellVisualKitModelAttachRec* attach) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006f94c0 в IDA Pro / Ghidra
