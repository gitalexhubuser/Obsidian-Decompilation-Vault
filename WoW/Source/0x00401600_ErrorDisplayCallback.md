---
offset: "0x00401600"
module: "WoW/Source"
file: "WoW/Source/Client_CVar.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00401600 — `ErrorDisplayCallback`

- **Адрес (Offset):** `0x00401600`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Client_CVar.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00401600
static bool ErrorDisplayCallback(CVar* var, const char* oldValue, const char* value, void* arg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00401600 в IDA Pro / Ghidra
