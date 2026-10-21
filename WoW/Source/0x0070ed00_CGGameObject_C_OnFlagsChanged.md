---
offset: "0x0070ed00"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/GameObject_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0070ed00 — `CGGameObject_C_OnFlagsChanged`

- **Адрес (Offset):** `0x0070ed00`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/GameObject_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0070ed00
int32_t CGGameObject_C::OnFlagsChanged(WOWGUID guid, uint32_t fieldOffset, uint32_t fieldSize, const void* oldValue, void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0070ed00 в IDA Pro / Ghidra
