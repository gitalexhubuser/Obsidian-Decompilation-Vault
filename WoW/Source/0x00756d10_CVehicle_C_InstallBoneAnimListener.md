---
offset: "0x00756d10"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Vehicle_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00756d10 — `CVehicle_C_InstallBoneAnimListener`

- **Адрес (Offset):** `0x00756d10`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Vehicle_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00756d10
int32_t CVehicle_C::InstallBoneAnimListener(WOWGUID guid, uint32_t boneId, void (*callback)(CGUnit_C* unit, int32_t& a2, TSGrowableArray<CVehiclePassenger_C*>& passengers)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00756d10 в IDA Pro / Ghidra
