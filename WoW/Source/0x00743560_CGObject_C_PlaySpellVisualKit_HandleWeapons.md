---
offset: "0x00743560"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Object_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00743560 — `CGObject_C_PlaySpellVisualKit_HandleWeapons`

- **Адрес (Offset):** `0x00743560`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Object_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00743560
void CGObject_C::PlaySpellVisualKit_HandleWeapons(const SpellRec* spell, const SpellVisualKitRec* kit, const C3Vector* position, WOWGUID guid, uint32_t a5, uint32_t flags, void (*callback)(CM2Model*, uint32_t, uint32_t, int32_t, uint32_t, uint64_t), int32_t* hasEffect) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00743560 в IDA Pro / Ghidra
