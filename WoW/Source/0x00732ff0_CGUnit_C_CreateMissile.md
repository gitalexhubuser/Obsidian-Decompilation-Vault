---
offset: "0x00732ff0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Unit_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00732ff0 — `CGUnit_C_CreateMissile`

- **Адрес (Offset):** `0x00732ff0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Unit_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00732ff0
void CGUnit_C::CreateMissile(const WOWGUID* target, PendingSpellCastData* data, uint32_t ammoDisplayId, uint32_t ammoInventoryType, int32_t hit, uint32_t missReason, uint32_t reflectResult, const SpellVisualRec* visual, int32_t spellId, const TSStackArray<WOWGUID>* targets, const TSStackArray<uint32_t>* missReasons, const TSStackArray<uint32_t>* reflectResults, uint32_t delay) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00732ff0 в IDA Pro / Ghidra
