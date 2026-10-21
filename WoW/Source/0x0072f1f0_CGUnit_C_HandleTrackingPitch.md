---
offset: "0x0072f1f0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Unit_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0072f1f0 — `CGUnit_C_HandleTrackingPitch`

- **Адрес (Offset):** `0x0072f1f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Unit_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0072f1f0
bool CGUnit_C::HandleTrackingPitch(float targetZ, float z, float pitch, float maxStep, uint32_t time, bool* overshoot) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0072f1f0 в IDA Pro / Ghidra
