---
offset: "0x0081daf0"
module: "Engine/Source"
file: "Engine/Source/Model2/M2Scene.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0081daf0 — `CM2Scene_HitTestGeometry`

- **Адрес (Offset):** `0x0081daf0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Model2/M2Scene.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0081daf0
M2HitRec* CM2Scene::HitTestGeometry(const CM2Model* model, uint32_t pass, const C3Vector& dir, float d, const C3Vector& start, M2HitRec* rec, float& t, M2HitRec* best) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0081daf0 в IDA Pro / Ghidra
