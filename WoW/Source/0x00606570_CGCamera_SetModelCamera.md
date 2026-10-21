---
offset: "0x00606570"
module: "WoW/Source"
file: "WoW/Source/UIUtil/Camera.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00606570 — `CGCamera_SetModelCamera`

- **Адрес (Offset):** `0x00606570`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/UIUtil/Camera.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00606570
int32_t CGCamera::SetModelCamera(const char* fileName, const C3Vector* position, float facing, void (*callback)(CM2Model* model, uint32_t boneId, uint32_t sequenceId, int32_t interrupted, uint32_t time, uint64_t param), uint64_t param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00606570 в IDA Pro / Ghidra
