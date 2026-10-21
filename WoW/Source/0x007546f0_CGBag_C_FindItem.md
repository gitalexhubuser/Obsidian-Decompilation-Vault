---
offset: "0x007546f0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Bag_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007546f0 — `CGBag_C_FindItem`

- **Адрес (Offset):** `0x007546f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Bag_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007546f0
CGItem_C* CGBag_C::FindItem(int32_t (*callback)(const CGItem_C* item, void* param), void* param, WOWGUID& container, uint32_t& slot, uint32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007546f0 в IDA Pro / Ghidra
