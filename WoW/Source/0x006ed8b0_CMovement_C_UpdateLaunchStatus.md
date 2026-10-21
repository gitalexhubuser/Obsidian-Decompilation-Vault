---
offset: "0x006ed8b0"
module: "WoW/Source"
file: "WoW/Source/Object/Movement.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006ed8b0 — `CMovement_C_UpdateLaunchStatus`

- **Адрес (Offset):** `0x006ed8b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/Movement.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006ed8b0
int32_t CMovement_C::UpdateLaunchStatus(uint32_t time, const CMovementStatus& status, MoveEventId eventId, const C2Vector& direction, float speed, float verticalSpeed) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006ed8b0 в IDA Pro / Ghidra
