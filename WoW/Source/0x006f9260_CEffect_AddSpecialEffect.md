---
offset: "0x006f9260"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Effect_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006f9260 — `CEffect_AddSpecialEffect`

- **Адрес (Offset):** `0x006f9260`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Effect_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006f9260
void CEffect::AddSpecialEffect(int32_t type, const WOWGUID& target, void (*callback)(CM2Model* model, uint32_t boneId, uint32_t sequenceId, int32_t interrupted, uint32_t time, uint64_t param)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006f9260 в IDA Pro / Ghidra
