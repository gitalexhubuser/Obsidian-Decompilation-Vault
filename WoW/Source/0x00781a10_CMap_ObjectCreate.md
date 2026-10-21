---
offset: "0x00781a10"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00781a10 — `CMap_ObjectCreate`

- **Адрес (Offset):** `0x00781a10`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00781a10
CMapEntity* CMap::ObjectCreate(CM2Model* model, MAP_OBJECT_FUNC func, void* funcParam, uint64_t param64, uintptr_t param32, uint32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00781a10 в IDA Pro / Ghidra
