---
offset: "0x00704af0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/DynamicObject_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00704af0 — `AnimFinishedCallback`

- **Адрес (Offset):** `0x00704af0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/DynamicObject_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00704af0
static void AnimFinishedCallback(CM2Model* model, uint32_t boneId, uint32_t sequenceId, int32_t interrupted, uint32_t time, uint64_t param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00704af0 в IDA Pro / Ghidra
