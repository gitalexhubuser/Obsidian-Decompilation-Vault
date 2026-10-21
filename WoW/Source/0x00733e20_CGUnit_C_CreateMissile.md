---
offset: "0x00733e20"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Unit_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00733e20 — `CGUnit_C_CreateMissile`

- **Адрес (Offset):** `0x00733e20`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Unit_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00733e20
void CGUnit_C::CreateMissile(const TSStackArray<SpellCastTargetPoint>* points, PendingSpellCastData* data, uint32_t ammoDisplayId, uint32_t ammoInventoryType, const SpellVisualRec* visual, int32_t spellId, uint32_t delay) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00733e20 в IDA Pro / Ghidra
