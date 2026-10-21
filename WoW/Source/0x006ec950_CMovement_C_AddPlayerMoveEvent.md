---
offset: "0x006ec950"
module: "WoW/Source"
file: "WoW/Source/Object/Movement.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006ec950 — `CMovement_C_AddPlayerMoveEvent`

- **Адрес (Offset):** `0x006ec950`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/Movement.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006ec950
void CMovement_C::AddPlayerMoveEvent(uint32_t eventTime, MoveEventId eventId, bool needAck, uint32_t ackCounter, const C2Vector& direction, float speed, float verticalSpeed, const CMovementStatus* status) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006ec950 в IDA Pro / Ghidra
