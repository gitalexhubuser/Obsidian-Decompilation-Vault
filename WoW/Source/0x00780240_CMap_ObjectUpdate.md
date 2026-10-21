---
offset: "0x00780240"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00780240 — `CMap_ObjectUpdate`

- **Адрес (Offset):** `0x00780240`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00780240
void CMap::ObjectUpdate(CMapEntity* entity, C44Matrix& mat, CAaBox& box, CAaSphere& sphere, C3Vector& vec, bool a6, uint32_t a7) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00780240 в IDA Pro / Ghidra
