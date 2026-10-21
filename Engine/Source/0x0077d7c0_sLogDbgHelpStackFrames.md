---
offset: "0x0077d7c0"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/MachineState.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0077d7c0 — `sLogDbgHelpStackFrames`

- **Адрес (Offset):** `0x0077d7c0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/MachineState.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077d7c0
static void sLogDbgHelpStackFrames(STACKFRAME* stackFrame, HANDLE process, HANDLE thread, uint32_t logOptions, void (*logLineProc)(void*, const char*, ...), void* logLineProcParam, CONTEXT* context, uint32_t stackFramesToSkip) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077d7c0 в IDA Pro / Ghidra
