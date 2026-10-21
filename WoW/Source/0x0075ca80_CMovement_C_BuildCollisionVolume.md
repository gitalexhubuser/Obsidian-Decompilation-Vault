---
offset: "0x0075ca80"
module: "WoW/Source"
file: "WoW/Source/Object/Movement.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0075ca80 — `CMovement_C_BuildCollisionVolume`

- **Адрес (Offset):** `0x0075ca80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/Movement.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0075ca80
void CMovement_C::BuildCollisionVolume(const C3Vector& position, float height, C4Plane* planes, C3Vector* points, uint8_t* faces) const {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0075ca80 в IDA Pro / Ghidra
