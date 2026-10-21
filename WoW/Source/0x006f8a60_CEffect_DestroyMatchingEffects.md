---
offset: "0x006f8a60"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Effect_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006f8a60 — `CEffect_DestroyMatchingEffects`

- **Адрес (Offset):** `0x006f8a60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Effect_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006f8a60
void __stdcall CEffect::DestroyMatchingEffects(CGObject_C* object, const SpellVisualEffectNameRec* effectName, int32_t attachType, int32_t spellId, int32_t kitId, const SpellVisualKitModelAttachRec* attach) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006f8a60 в IDA Pro / Ghidra
