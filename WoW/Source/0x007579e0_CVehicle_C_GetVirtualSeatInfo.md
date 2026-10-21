---
offset: "0x007579e0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Vehicle_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007579e0 — `CVehicle_C_GetVirtualSeatInfo`

- **Адрес (Offset):** `0x007579e0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Vehicle_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007579e0
int32_t CVehicle_C::GetVirtualSeatInfo(int32_t virtualSeat, const char*& type, const char*& occupant, const char*& realm, int32_t& canEject, int32_t& canSwitch) const {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007579e0 в IDA Pro / Ghidra
