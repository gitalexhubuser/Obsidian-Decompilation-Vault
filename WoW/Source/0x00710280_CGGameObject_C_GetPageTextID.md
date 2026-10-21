---
offset: "0x00710280"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/GameObject_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00710280 — `CGGameObject_C_GetPageTextID`

- **Адрес (Offset):** `0x00710280`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/GameObject_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00710280
int32_t CGGameObject_C::GetPageTextID(void (*callback)(int32_t, const WOWGUID&, void*, bool)) const {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00710280 в IDA Pro / Ghidra
