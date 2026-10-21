---
offset: "0x006ecf80"
module: "WoW/Source"
file: "WoW/Source/Object/Movement.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006ecf80 — `CMovement_C_Teleport`

- **Адрес (Offset):** `0x006ecf80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/Movement.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006ecf80
void CMovement_C::Teleport(WOWGUID transport, const C3Vector& position, float facing, int32_t removeSpline, int32_t needAck, uint8_t seat) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006ecf80 в IDA Pro / Ghidra
