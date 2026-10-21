---
offset: "0x0077cf00"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/MachineState.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0077cf00 — `sLogDateTimeString`

- **Адрес (Offset):** `0x0077cf00`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/MachineState.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077cf00
static void sLogDateTimeString(void (*logLineProc)(void*, const char*, ...), void* logLineProcParam, const SYSTEMTIME* time) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077cf00 в IDA Pro / Ghidra
