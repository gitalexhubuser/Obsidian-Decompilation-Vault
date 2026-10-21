---
offset: "0x007086b0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Item_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007086b0 — `CGItem_C_IsLocked`

- **Адрес (Offset):** `0x007086b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Item_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007086b0
int32_t CGItem_C::IsLocked(const LockRec* lock, int32_t itemLevel, int32_t* spellId, int32_t* skillValue, int32_t* requiredSkill, int32_t* lockIndex, CGItem_C** key, int32_t* entry) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007086b0 в IDA Pro / Ghidra
