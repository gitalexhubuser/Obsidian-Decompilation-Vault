---
offset: "0x00781c90"
module: "WoW/Source"
file: "WoW/Source/WorldClient/World.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00781c90 — `CMap_ObjectCreateStaticEx`

- **Адрес (Offset):** `0x00781c90`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/World.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00781c90
CMapEntity* CMap::ObjectCreateStaticEx(CM2Model* model, const C44Matrix& matrix, MAP_OBJECT_FUNC func, void* funcParam, uint64_t param64, uintptr_t param32, const char* file, int32_t line) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00781c90 в IDA Pro / Ghidra
