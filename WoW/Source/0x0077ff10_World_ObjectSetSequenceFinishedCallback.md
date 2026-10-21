---
offset: "0x0077ff10"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0077ff10 — `World_ObjectSetSequenceFinishedCallback`

- **Адрес (Offset):** `0x0077ff10`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077ff10
void World::ObjectSetSequenceFinishedCallback(CMapEntity* entity, void (*callback)(CM2Model* model, uint32_t boneId, uint32_t sequenceId, int32_t interrupted, uint32_t time, uint64_t param), uint64_t param, uint16_t doodad) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077ff10 в IDA Pro / Ghidra
