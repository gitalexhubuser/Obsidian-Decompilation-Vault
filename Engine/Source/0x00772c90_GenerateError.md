---
offset: "0x00772c90"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SCmd.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00772c90 — `GenerateError`

- **Адрес (Offset):** `0x00772c90`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SCmd.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00772c90
void GenerateError(void (STORMAPI* errorcallback)(_CMDERROR*), uint32_t errorcode, const char* itemstring) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00772c90 в IDA Pro / Ghidra
