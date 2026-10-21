---
offset: "0x007124b0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/GameObject_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007124b0 — `CGGameObject_C_TypeAnimated_CGGameObject_C_TypeAnimated`

- **Адрес (Offset):** `0x007124b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/GameObject_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007124b0
CGGameObject_C_TypeAnimated::CGGameObject_C_TypeAnimated(CGGameObject_C* owner) : CGGameObject_C_TypeBase(owner), m_animState(-1), m_pendingAnimState(-1), m_nextAnimTime(-1) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007124b0 в IDA Pro / Ghidra
