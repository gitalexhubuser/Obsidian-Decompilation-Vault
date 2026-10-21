---
offset: "0x00772da0"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SCmd.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00772da0 — `ProcessFile`

- **Адрес (Offset):** `0x00772da0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SCmd.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00772da0
int32_t ProcessFile(const char* filename, _PROCESSING* processing, CMDDEF** nextarg, int32_t (STORMAPI* extracallback)(const char*), void (STORMAPI* errorcallback)(_CMDERROR*)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00772da0 в IDA Pro / Ghidra
