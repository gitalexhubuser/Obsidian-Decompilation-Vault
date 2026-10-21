---
offset: "0x0082e720"
module: "Engine/Source"
file: "Engine/Source/Model2/M2Model.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0082e720 — `CM2Model_SequenceCallback`

- **Адрес (Offset):** `0x0082e720`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Model2/M2Model.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0082e720
int32_t __stdcall CM2Model::SequenceCallback(void* callback, CM2Model* model, uint32_t boneId, uint32_t sequenceId, int32_t interrupted, uint32_t time, uint32_t sequenceIndex, uint32_t startTime, uint64_t param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0082e720 в IDA Pro / Ghidra
