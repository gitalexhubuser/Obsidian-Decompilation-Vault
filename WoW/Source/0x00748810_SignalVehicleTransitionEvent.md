---
offset: "0x00748810"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/VehiclePassenger_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00748810 — `SignalVehicleTransitionEvent`

- **Адрес (Offset):** `0x00748810`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/VehiclePassenger_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00748810
static void SignalVehicleTransitionEvent(WOWGUID guid, const VehicleRec* vehicleRec, const VehicleSeatRec* seatRec, uint32_t event) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00748810 в IDA Pro / Ghidra
