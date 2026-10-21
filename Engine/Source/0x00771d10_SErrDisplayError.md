---
offset: "0x00771d10"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SErr.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00771d10 — `SErrDisplayError`

- **Адрес (Offset):** `0x00771d10`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SErr.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00771d10
int32_t STORMAPI SErrDisplayError(uint32_t errorcode, const char* filename, int32_t linenumber, const char* description, int32_t recoverable, uint32_t exitcode, uint32_t unknown) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00771d10 в IDA Pro / Ghidra
