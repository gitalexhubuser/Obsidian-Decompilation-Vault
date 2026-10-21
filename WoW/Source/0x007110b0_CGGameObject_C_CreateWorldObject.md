---
offset: "0x007110b0"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/GameObject_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007110b0 — `CGGameObject_C_CreateWorldObject`

- **Адрес (Offset):** `0x007110b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/GameObject_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007110b0
CMapEntity* CGGameObject_C::CreateWorldObject(uint64_t guid, int32_t a4, uint32_t doodadSetCount, const int16_t* doodadSets) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007110b0 в IDA Pro / Ghidra
