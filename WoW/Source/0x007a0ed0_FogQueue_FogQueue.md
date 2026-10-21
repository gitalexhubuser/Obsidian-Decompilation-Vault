---
offset: "0x007a0ed0"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapEntity.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007a0ed0 — `FogQueue_FogQueue`

- **Адрес (Offset):** `0x007a0ed0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapEntity.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007a0ed0
FogQueue::FogQueue(const uint32_t* params) : CMemBlock(sizeof(FogQ) * params[0], 0, typeid(FogQ).raw_name(), SLOG_OBJECT) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007a0ed0 в IDA Pro / Ghidra
