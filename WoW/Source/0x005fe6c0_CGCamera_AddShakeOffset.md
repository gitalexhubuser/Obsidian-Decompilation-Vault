---
offset: "0x005fe6c0"
module: "WoW/Source"
file: "WoW/Source/UIUtil/Camera.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x005fe6c0 — `CGCamera_AddShakeOffset`

- **Адрес (Offset):** `0x005fe6c0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/UIUtil/Camera.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x005fe6c0
void CGCamera::AddShakeOffset(C3Vector& offset, float facing, float amplitude, float time, float frequency, int32_t type, float damping, CGCameraDir dir) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x005fe6c0 в IDA Pro / Ghidra
