---
offset: "0x00714250"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/GameObject_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00714250 — `CGGameObject_C_CGGameObject_C`

- **Адрес (Offset):** `0x00714250`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/GameObject_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00714250
CGGameObject_C::CGGameObject_C(uint32_t time, const CClientObjCreate& create) : CGObject_C(time, create), m_passenger(create.m_move.m_status.m_transportGuid, create.m_move.m_status.m_transportPosition, this->m_obj->m_guid), m_typeData(nullptr), m_stats(nullptr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00714250 в IDA Pro / Ghidra
