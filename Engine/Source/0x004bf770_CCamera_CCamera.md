---
offset: "0x004bf770"
module: "Engine/Source"
file: "Engine/Source/Services/Camera.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004bf770 — `CCamera_CCamera`

- **Адрес (Offset):** `0x004bf770`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Services/Camera.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004bf770
CCamera::CCamera() : CDataMgr(9), m_position(C3Vector(100.0f, 0.0f, 0.0f)), m_target(C3Vector(0.0f, 0.0f, 0.0f)), m_distance(100.0f), m_zFar(5000.0f), m_zNear(8.0f), m_aoa(0.0f), m_fov(1.5707964f), m_roll(0.0f), m_rotation(0.0f) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004bf770 в IDA Pro / Ghidra
