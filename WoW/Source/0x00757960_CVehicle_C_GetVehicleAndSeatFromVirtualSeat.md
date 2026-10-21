---
offset: "0x00757960"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Vehicle_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00757960 — `CVehicle_C_GetVehicleAndSeatFromVirtualSeat`

- **Адрес (Offset):** `0x00757960`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Vehicle_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00757960
int32_t CVehicle_C::GetVehicleAndSeatFromVirtualSeat(int32_t virtualSeat, const CVehicle_C*& vehicle, uint8_t& seat) const {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00757960 в IDA Pro / Ghidra
