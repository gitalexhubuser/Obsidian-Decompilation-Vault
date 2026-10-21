---
offset: "0x004017c0"
module: "WoW/Source"
file: "WoW/Source/Client_CVar.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004017c0 — `ErrorDisplayMinLevelCallback`

- **Адрес (Offset):** `0x004017c0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Client_CVar.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004017c0
static bool ErrorDisplayMinLevelCallback(CVar* var, const char* oldValue, const char* value, void* arg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004017c0 в IDA Pro / Ghidra
