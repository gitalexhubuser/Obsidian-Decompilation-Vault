---
offset: "0x00749fb0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/VehiclePassenger_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00749fb0 — `CVehiclePassenger_C_SendTransitionUIEvents`

- **Адрес (Offset):** `0x00749fb0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/VehiclePassenger_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00749fb0
void CVehiclePassenger_C::SendTransitionUIEvents(WOWGUID guid, const VehicleRec* vehicleRec, const VehicleSeatRec* seatRec, int32_t fromState, int32_t toState) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00749fb0 в IDA Pro / Ghidra
