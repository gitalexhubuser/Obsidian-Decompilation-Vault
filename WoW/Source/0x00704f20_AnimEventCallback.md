---
offset: "0x00704f20"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/DynamicObject_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00704f20 — `AnimEventCallback`

- **Адрес (Offset):** `0x00704f20`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/DynamicObject_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00704f20
static void AnimEventCallback(CM2Model* model, uint32_t boneId, uint32_t eventId, uint32_t data, const C3Vector* position, uint32_t time, uint64_t param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00704f20 в IDA Pro / Ghidra
