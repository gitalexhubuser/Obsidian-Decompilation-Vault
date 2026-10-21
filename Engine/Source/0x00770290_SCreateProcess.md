---
offset: "0x00770290"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SThread.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00770290 — `SCreateProcess`

- **Адрес (Offset):** `0x00770290`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SThread.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00770290
int32_t STORMAPI SCreateProcess(const char* appName, char* commandLine, void (*callbackWhenProcessCompletes)(void*), void* callbackData) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00770290 в IDA Pro / Ghidra
