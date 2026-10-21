---
offset: "0x006ec8b0"
module: "WoW/Source"
file: "WoW/Source/Object/Movement.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006ec8b0 — `CMovement_C_AddPlayerSpeedEvent`

- **Адрес (Offset):** `0x006ec8b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/Movement.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006ec8b0
void CMovement_C::AddPlayerSpeedEvent(uint32_t eventTime, MoveEventId eventId, bool needAck, uint32_t ackCounter, float value, const CMovementStatus* status) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006ec8b0 в IDA Pro / Ghidra
