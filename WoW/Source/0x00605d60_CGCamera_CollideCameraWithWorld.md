---
offset: "0x00605d60"
module: "WoW/Source"
file: "WoW/Source/UIUtil/Camera.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00605d60 — `CGCamera_CollideCameraWithWorld`

- **Адрес (Offset):** `0x00605d60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/UIUtil/Camera.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00605d60
uint32_t CGCamera::CollideCameraWithWorld(const C3Vector& target, float& distance, float& height, const C3Vector& offset, float liquid, float& extent) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00605d60 в IDA Pro / Ghidra
