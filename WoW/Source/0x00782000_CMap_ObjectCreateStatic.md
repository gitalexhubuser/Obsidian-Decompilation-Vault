---
offset: "0x00782000"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00782000 — `CMap_ObjectCreateStatic`

- **Адрес (Offset):** `0x00782000`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00782000
CMapEntity* CMap::ObjectCreateStatic(CM2Model* model, const C44Matrix& matrix, MAP_OBJECT_FUNC func, void* funcParam, uintptr_t param32) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00782000 в IDA Pro / Ghidra
