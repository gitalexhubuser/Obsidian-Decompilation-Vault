---
offset: "0x00760fc0"
module: "WoW/Source"
file: "WoW/Source/Object/Movement.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00760fc0 — `CMovement_C_TryFallingDown`

- **Адрес (Offset):** `0x00760fc0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/Movement.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00760fc0
int32_t CMovement_C::TryFallingDown(float timeFallen, C3Vector* move, float* distance, C2Vector* push, uint64_t* facetId, int32_t* onSlope, int32_t* landed) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00760fc0 в IDA Pro / Ghidra
