---
offset: "0x00735820"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Unit_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00735820 — `CGUnit_C_SetKeyBoneSequence`

- **Адрес (Offset):** `0x00735820`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Unit_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00735820
void CGUnit_C::SetKeyBoneSequence(CM2Model* model, uint32_t boneId, uint32_t sequenceId, uint32_t variation, uint32_t time, float speed, int32_t blend, int32_t primary, int32_t force) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00735820 в IDA Pro / Ghidra
