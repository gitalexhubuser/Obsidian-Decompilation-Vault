---
offset: "0x007432e0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Object_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007432e0 — `CGObject_C_GetAppropriateSpellVisual`

- **Адрес (Offset):** `0x007432e0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Object_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007432e0
const SpellVisualRec* CGObject_C::GetAppropriateSpellVisual(const SpellRec* spell, SpellVisualRec& visual, int32_t visualId, int32_t lowViolenceVisualId) const {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007432e0 в IDA Pro / Ghidra
