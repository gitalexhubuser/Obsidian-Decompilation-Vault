---
offset: "0x00741a00"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Unit_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00741a00 — `DynamicFlagsChangeHandler`

- **Адрес (Offset):** `0x00741a00`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Unit_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00741a00
int32_t DynamicFlagsChangeHandler(WOWGUID guid, uint32_t fieldOffset, uint32_t fieldSize, const void* oldValue, void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00741a00 в IDA Pro / Ghidra
