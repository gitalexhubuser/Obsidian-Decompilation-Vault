---
offset: "0x00754cd0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Bag_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00754cd0 — `CGBag_C_FindItem`

- **Адрес (Offset):** `0x00754cd0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Bag_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00754cd0
CGItem_C* CGBag_C::FindItem(int32_t (*callback)(const CGItem_C* item, void* param), void* param, uint32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00754cd0 в IDA Pro / Ghidra
