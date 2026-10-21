---
offset: "0x007bd5a0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapLoad.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007bd5a0 — `CMapStaticEntity_ModelEventCallback`

- **Адрес (Offset):** `0x007bd5a0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapLoad.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007bd5a0
void CMapStaticEntity::ModelEventCallback(CM2Model* model, uint32_t boneId, uint32_t eventId, uint32_t data, const C3Vector* position, uint32_t time, uint64_t param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007bd5a0 в IDA Pro / Ghidra
