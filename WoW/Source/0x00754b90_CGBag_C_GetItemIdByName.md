---
offset: "0x00754b90"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Bag_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00754b90 — `CGBag_C_GetItemIdByName`

- **Адрес (Offset):** `0x00754b90`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Bag_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00754b90
CGItem_C* CGBag_C::GetItemIdByName(const char* name, WOWGUID& container, uint32_t& slot, uint32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00754b90 в IDA Pro / Ghidra
