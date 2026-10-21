---
offset: "0x007711c0"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SErr.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x007711c0 — `CreateErrorLogFile`

- **Адрес (Offset):** `0x007711c0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SErr.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007711c0
static HANDLE CreateErrorLogFile(const char* suffix, const char* ext, char* logpath, uint32_t logpathchars, const SYSTEMTIME* time) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007711c0 в IDA Pro / Ghidra
