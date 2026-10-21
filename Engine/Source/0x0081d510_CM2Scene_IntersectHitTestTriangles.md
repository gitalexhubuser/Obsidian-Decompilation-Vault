---
offset: "0x0081d510"
module: "Engine/Source"
file: "Engine/Source/Model2/M2Scene.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0081d510 — `CM2Scene_IntersectHitTestTriangles`

- **Адрес (Offset):** `0x0081d510`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Model2/M2Scene.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0081d510
M2HitRec* CM2Scene::IntersectHitTestTriangles(const uint16_t* indices, const uint16_t* end, uint32_t vertexStart, const C3Vector& start, uint32_t pass, M2HitRec* rec, float& t, M2HitRec* best) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0081d510 в IDA Pro / Ghidra
