---
offset: "0x006004b0"
module: "WoW/Source"
file: "WoW/Source/UIUtil/Camera.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006004b0 — `ComputeShakeFalloff`

- **Адрес (Offset):** `0x006004b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/UIUtil/Camera.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006004b0
static int32_t __stdcall ComputeShakeFalloff(const C3Vector& position, const C3Vector& shakePosition, float& amplitude, float start, float startSqr, float max, float maxSqr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006004b0 в IDA Pro / Ghidra
