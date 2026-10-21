---
offset: "0x0077ff60"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0077ff60 — `World_ObjectSetEventCallback`

- **Адрес (Offset):** `0x0077ff60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077ff60
void World::ObjectSetEventCallback(CMapBaseObj* object, void (*callback)(CM2Model* model, uint32_t boneId, uint32_t eventId, uint32_t data, const C3Vector* position, uint32_t time, uint64_t param), uint64_t param, uint16_t doodadSet) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077ff60 в IDA Pro / Ghidra
