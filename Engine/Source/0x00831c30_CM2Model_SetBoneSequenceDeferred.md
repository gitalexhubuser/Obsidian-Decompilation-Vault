---
offset: "0x00831c30"
module: "Engine/Source"
file: "Engine/Source/Model2/M2Model.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00831c30 — `CM2Model_SetBoneSequenceDeferred`

- **Адрес (Offset):** `0x00831c30`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Model2/M2Model.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00831c30
void CM2Model::SetBoneSequenceDeferred(uint16_t sequenceIndex, M2Data* data, uint16_t boneIndex, uint32_t time, float speed, M2SequenceFallback fallback, int32_t blend, int32_t primary, int32_t pickRandom) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00831c30 в IDA Pro / Ghidra
