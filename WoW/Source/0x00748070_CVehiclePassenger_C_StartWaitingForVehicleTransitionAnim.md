---
offset: "0x00748070"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/VehiclePassenger_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00748070 — `CVehiclePassenger_C_StartWaitingForVehicleTransitionAnim`

- **Адрес (Offset):** `0x00748070`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/VehiclePassenger_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00748070
void CVehiclePassenger_C::StartWaitingForVehicleTransitionAnim(WOWGUID guid, uint8_t seat, const VehicleSeatRec* seatRec, int32_t entering, CVehicle_C* vehicle) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00748070 в IDA Pro / Ghidra
