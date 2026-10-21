---
offset: "0x006f93a0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Effect_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006f93a0 — `CEffect_AddSpecialByPosition`

- **Адрес (Offset):** `0x006f93a0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Effect_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006f93a0
void CEffect::AddSpecialByPosition(int32_t type, C3Vector position, const WOWGUID* guid, uint32_t flags, void (*callback)(CM2Model* model, uint32_t boneId, uint32_t sequenceId, int32_t interrupted, uint32_t time, uint64_t param)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006f93a0 в IDA Pro / Ghidra
