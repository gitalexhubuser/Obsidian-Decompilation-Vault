---
offset: "0x0073a6c0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Unit_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0073a6c0 — `CGUnit_C_PlaySpellVisualKit_HandleWeapons`

- **Адрес (Offset):** `0x0073a6c0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Unit_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0073a6c0
void CGUnit_C::PlaySpellVisualKit_HandleWeapons(const SpellRec* spell, const SpellVisualKitRec* kit, const C3Vector* position, WOWGUID guid, uint32_t a5, uint32_t flags, void (*callback)(CM2Model*, uint32_t, uint32_t, int32_t, uint32_t, uint64_t), int32_t* hasEffect) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0073a6c0 в IDA Pro / Ghidra
