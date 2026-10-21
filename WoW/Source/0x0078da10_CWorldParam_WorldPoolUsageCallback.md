---
offset: "0x0078da10"
module: "WoW/Source"
file: "WoW/Source/WorldClient/WorldParam_CVar.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0078da10 — `CWorldParam_WorldPoolUsageCallback`

- **Адрес (Offset):** `0x0078da10`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/WorldParam_CVar.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0078da10
bool CWorldParam::WorldPoolUsageCallback(CVar* var, const char* oldValue, const char* value, void* arg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0078da10 в IDA Pro / Ghidra
