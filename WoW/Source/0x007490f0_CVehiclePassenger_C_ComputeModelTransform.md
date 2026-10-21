---
offset: "0x007490f0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/VehiclePassenger_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007490f0 — `CVehiclePassenger_C_ComputeModelTransform`

- **Адрес (Offset):** `0x007490f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/VehiclePassenger_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007490f0
void CVehiclePassenger_C::ComputeModelTransform(C44Matrix& matrix, CM2Model*& model, CGUnit_C* vehicle, const VehicleSeatRec* seat, uint32_t attachment, float facing) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007490f0 в IDA Pro / Ghidra
