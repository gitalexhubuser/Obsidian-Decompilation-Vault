---
offset: "0x006fa5b0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Effect_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006fa5b0 — `CEffect_AddLootEffect`

- **Адрес (Offset):** `0x006fa5b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Effect_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006fa5b0
void CEffect::AddLootEffect(CGUnit_C* unit, void (*callback)(CM2Model* model, uint32_t boneId, uint32_t sequenceId, int32_t interrupted, uint32_t time, uint64_t param)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006fa5b0 в IDA Pro / Ghidra
