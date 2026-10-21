---
offset: "0x0070f160"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/GameObject_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0070f160 — `CGGameObject_C_IsLocked`

- **Адрес (Offset):** `0x0070f160`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/GameObject_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0070f160
bool CGGameObject_C::IsLocked(int32_t* spellId, int32_t* skillValue, int32_t* requiredSkill, CGItem_C** key, uint32_t* entry) const {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0070f160 в IDA Pro / Ghidra
