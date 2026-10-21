---
offset: "0x00744790"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Object_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00744790 — `CGObject_C_PlayEffectName`

- **Адрес (Offset):** `0x00744790`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Object_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00744790
void CGObject_C::PlayEffectName(int32_t attachType, uint32_t a3, int32_t spellId, const SpellVisualKitRec* kit, const SpellVisualEffectNameRec* effectName, uint32_t* flags, void (*callback)(CM2Model*, uint32_t, uint32_t, int32_t, uint32_t, uint64_t), const C3Vector* position, WOWGUID target, uint32_t a11, const SpellVisualKitModelAttachRec* attach) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00744790 в IDA Pro / Ghidra
