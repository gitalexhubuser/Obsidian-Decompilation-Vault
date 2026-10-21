---
offset: "0x005f7e90"
module: "WoW/Source"
file: "WoW/Source/UIUtil/AddOns.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x005f7e90 — `IsAddOnLoadable`

- **Адрес (Offset):** `0x005f7e90`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/UIUtil/AddOns.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x005f7e90
bool IsAddOnLoadable(const char* name, bool demandLoad, UIADDON_LOADABLE_REASON& reason, UIADDON_LOADABLE_REASON& dependencyReason, const char* character) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x005f7e90 в IDA Pro / Ghidra
