---
offset: "0x00760720"
module: "WoW/Source"
file: "WoW/Source/Object/Movement.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00760720 — `CMovement_C_CollideWithTransport`

- **Адрес (Offset):** `0x00760720`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/Movement.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00760720
void CMovement_C::CollideWithTransport(uint32_t time, uint32_t elapsed, float distance, const C3Vector& direction, const C44Matrix& transportMatrix) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00760720 в IDA Pro / Ghidra
