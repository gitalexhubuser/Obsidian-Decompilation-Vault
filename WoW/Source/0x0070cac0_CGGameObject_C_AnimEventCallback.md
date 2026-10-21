---
offset: "0x0070cac0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/GameObject_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0070cac0 — `CGGameObject_C_AnimEventCallback`

- **Адрес (Offset):** `0x0070cac0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/GameObject_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0070cac0
void CGGameObject_C::AnimEventCallback(CM2Model* model, uint32_t boneId, uint32_t eventId, uint32_t data, const C3Vector* position, uint32_t time, uint64_t param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0070cac0 в IDA Pro / Ghidra
