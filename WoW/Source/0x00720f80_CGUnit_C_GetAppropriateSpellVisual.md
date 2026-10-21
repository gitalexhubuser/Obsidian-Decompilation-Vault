---
offset: "0x00720f80"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Unit_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00720f80 — `CGUnit_C_GetAppropriateSpellVisual`

- **Адрес (Offset):** `0x00720f80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Unit_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00720f80
const SpellVisualRec* CGUnit_C::GetAppropriateSpellVisual(const SpellRec* spell, SpellVisualRec& visual, int32_t visualId, int32_t lowViolenceVisualId) const {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00720f80 в IDA Pro / Ghidra
