---
offset: "0x00772ac0"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SErr.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00772ac0 — `SErrDisplayErrorFmt`

- **Адрес (Offset):** `0x00772ac0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SErr.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00772ac0
int32_t SErrDisplayErrorFmt(uint32_t errorcode, const char* filename, int32_t linenumber, int32_t recoverable, uint32_t exitcode, const char* format, ...) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00772ac0 в IDA Pro / Ghidra
