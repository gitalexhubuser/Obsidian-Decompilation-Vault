---
offset: "0x00773990"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SCmd.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00773990 — `SCmdProcessCommandLine`

- **Адрес (Offset):** `0x00773990`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SCmd.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00773990
int32_t STORMAPI SCmdProcessCommandLine(int32_t (STORMAPI* extracallback)(const char*), void (STORMAPI* errorcallback)(_CMDERROR*)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00773990 в IDA Pro / Ghidra
