---
offset: "0x0077f2c0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0077f2c0 — `World_ObjectSetUpdateCallback`

- **Адрес (Offset):** `0x0077f2c0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077f2c0
void World::ObjectSetUpdateCallback(CMapEntity* entity, int32_t (*func)(void*, uint32_t, uint64_t, uintptr_t), void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077f2c0 в IDA Pro / Ghidra
