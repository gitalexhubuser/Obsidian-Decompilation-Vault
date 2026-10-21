---
offset: "0x0070b2b0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/GameObject_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0070b2b0 — `CGGameObject_C_Type_WorldObj_SequenceFinishedHandler`

- **Адрес (Offset):** `0x0070b2b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/GameObject_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0070b2b0
void CGGameObject_C_Type_WorldObj::SequenceFinishedHandler(CM2Model* model, uint32_t boneId, uint32_t sequenceId, int32_t interrupted, uint32_t time, uint64_t param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0070b2b0 в IDA Pro / Ghidra
