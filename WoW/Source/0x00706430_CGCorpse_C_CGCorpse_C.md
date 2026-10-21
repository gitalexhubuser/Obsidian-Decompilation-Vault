---
offset: "0x00706430"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Corpse_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00706430 — `CGCorpse_C_CGCorpse_C`

- **Адрес (Offset):** `0x00706430`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Corpse_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00706430
CGCorpse_C::CGCorpse_C(uint32_t time, const CClientObjCreate& create) : CGObject_C(time, create), m_passenger(create.m_move.m_status.m_transportGuid, create.m_move.m_status.m_transportPosition, this->m_obj->m_guid), m_component(nullptr), m_groundNormal(0.0f, 0.0f, 1.0f), m_corpseFlags(0), m_selectionRadius(0.0f), m_lootEffect(nullptr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00706430 в IDA Pro / Ghidra
