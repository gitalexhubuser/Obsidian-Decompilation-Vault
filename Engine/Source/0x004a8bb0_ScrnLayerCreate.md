---
offset: "0x004a8bb0"
module: "Engine/Source"
file: "Engine/Source/Scrn/Layer.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004a8bb0 — `ScrnLayerCreate`

- **Адрес (Offset):** `0x004a8bb0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Scrn/Layer.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004a8bb0
void ScrnLayerCreate(const RECTF* rect, float zorder, uint32_t flags, void* param, void (*paintFunc)(void* param, const RECTF* rect, const RECTF* visible, float elapsedSec), HLAYER* layer) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004a8bb0 в IDA Pro / Ghidra
