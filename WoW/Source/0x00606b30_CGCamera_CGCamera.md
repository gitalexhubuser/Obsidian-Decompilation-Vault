---
offset: "0x00606b30"
module: "WoW/Source"
file: "WoW/Source/UIUtil/Camera.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00606b30 — `CGCamera_CGCamera`

- **Адрес (Offset):** `0x00606b30`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/UIUtil/Camera.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00606b30
CGCamera::CGCamera() : CSimpleCamera(World::s_nearClip, World::s_farClip, 1.5707964f) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00606b30 в IDA Pro / Ghidra
