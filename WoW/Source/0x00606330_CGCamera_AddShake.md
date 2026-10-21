---
offset: "0x00606330"
module: "WoW/Source"
file: "WoW/Source/UIUtil/Camera.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00606330 — `CGCamera_AddShake`

- **Адрес (Offset):** `0x00606330`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/UIUtil/Camera.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00606330
void CGCamera::AddShake(const C3Vector& position, int32_t type, CGCameraDir dir, float amplitude, float frequency, float duration, float timeOffset, float damping) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00606330 в IDA Pro / Ghidra
