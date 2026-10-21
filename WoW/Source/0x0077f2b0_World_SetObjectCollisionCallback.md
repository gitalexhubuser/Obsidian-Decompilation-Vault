---
offset: "0x0077f2b0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0077f2b0 — `World_SetObjectCollisionCallback`

- **Адрес (Offset):** `0x0077f2b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077f2b0
void World::SetObjectCollisionCallback(int32_t (*callback)(WOWGUID* guid, uintptr_t param, ObjectCollisionData* data, uint32_t flags)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077f2b0 в IDA Pro / Ghidra
