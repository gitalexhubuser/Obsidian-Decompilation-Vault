---
offset: "0x00713820"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/CGGameObject_C_Type_Transport.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00713820 — `CGGameObject_C_Type_Transport_CGGameObject_C_Type_Transport`

- **Адрес (Offset):** `0x00713820`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/CGGameObject_C_Type_Transport.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00713820
CGGameObject_C_Type_Transport::CGGameObject_C_Type_Transport(CGGameObject_C* owner) : CGGameObject_C_Type_TransportBase(owner), m_frames(nullptr), m_frameCount(0), m_currentFrame(0), m_rotations(nullptr), m_rotationCount(0), m_currentRotation(0), m_lastSequence(506), m_stateChangeSequenceTime(0) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00713820 в IDA Pro / Ghidra
