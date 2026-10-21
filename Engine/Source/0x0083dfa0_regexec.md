---
offset: "0x0083dfa0"
module: "Engine/Source"
file: "Engine/Source/pcre/pcreposix.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0083dfa0 — `regexec`

- **Адрес (Offset):** `0x0083dfa0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/pcre/pcreposix.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0083dfa0
int32_t regexec(const regex_t* preg, const char* string, size_t nmatch, regmatch_t pmatch[], int32_t eflags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0083dfa0 в IDA Pro / Ghidra
