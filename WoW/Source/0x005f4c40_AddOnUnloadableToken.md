---
offset: "0x005f4c40"
module: "WoW/Source"
file: "WoW/Source/UIUtil/AddOns.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x005f4c40 — `AddOnUnloadableToken`

- **Адрес (Offset):** `0x005f4c40`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/UIUtil/AddOns.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x005f4c40
char* AddOnUnloadableToken(UIADDON_LOADABLE_REASON reason, UIADDON_LOADABLE_REASON dependencyReason, char* buffer, uint32_t size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x005f4c40 в IDA Pro / Ghidra
