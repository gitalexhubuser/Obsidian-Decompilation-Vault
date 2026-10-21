---
offset: "0x0077cc10"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/MachineState.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0077cc10 — `sLogHeader`

- **Адрес (Offset):** `0x0077cc10`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/MachineState.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077cc10
static void sLogHeader(void (*logLineProc)(void*, const char*, ...), void* logLineProcParam, const char* headerString) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077cc10 в IDA Pro / Ghidra
