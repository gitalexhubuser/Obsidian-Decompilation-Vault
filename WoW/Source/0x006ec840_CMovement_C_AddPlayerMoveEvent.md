---
offset: "0x006ec840"
module: "WoW/Source"
file: "WoW/Source/Object/Movement.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006ec840 — `CMovement_C_AddPlayerMoveEvent`

- **Адрес (Offset):** `0x006ec840`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/Movement.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006ec840
void CMovement_C::AddPlayerMoveEvent(uint32_t eventTime, MoveEventId eventId, bool needAck, uint32_t ackCounter, float facing, float pitch, uint16_t extraFlags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006ec840 в IDA Pro / Ghidra
