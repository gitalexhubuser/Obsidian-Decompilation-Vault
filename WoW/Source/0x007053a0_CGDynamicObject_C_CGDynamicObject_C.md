---
offset: "0x007053a0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/DynamicObject_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007053a0 — `CGDynamicObject_C_CGDynamicObject_C`

- **Адрес (Offset):** `0x007053a0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/DynamicObject_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007053a0
CGDynamicObject_C::CGDynamicObject_C(uint32_t time, const CClientObjCreate& create) : CGObject_C(time, create), m_passenger(create.m_move.m_status.m_transportGuid, create.m_move.m_status.m_transportPosition, this->m_obj->m_guid), m_scale(1.0f), m_blizzardVisual(nullptr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007053a0 в IDA Pro / Ghidra
