---
offset: "0x00754a50"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Bag_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00754a50 — `CGBag_C_FindItemOfType`

- **Адрес (Offset):** `0x00754a50`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Bag_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00754a50
CGItem_C* CGBag_C::FindItemOfType(int32_t itemId, WOWGUID& container, uint32_t& slot, uint32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00754a50 в IDA Pro / Ghidra
