---
offset: "0x00401a10"
module: "WoW/Source"
file: "WoW/Source/Client_CVar.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00401a10 — `ErrorDisplayFilterCallback`

- **Адрес (Offset):** `0x00401a10`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Client_CVar.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00401a10
static bool ErrorDisplayFilterCallback(CVar* var, const char* oldValue, const char* value, void* arg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00401a10 в IDA Pro / Ghidra
