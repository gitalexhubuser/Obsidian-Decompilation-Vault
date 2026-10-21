---
offset: "0x00711050"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/GameObject_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00711050 — `CGGameObject_C_OnStateChanged`

- **Адрес (Offset):** `0x00711050`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/GameObject_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00711050
int32_t CGGameObject_C::OnStateChanged(WOWGUID guid, uint32_t fieldOffset, uint32_t fieldSize, const void* oldValue, void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00711050 в IDA Pro / Ghidra
