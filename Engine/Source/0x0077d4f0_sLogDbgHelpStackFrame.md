---
offset: "0x0077d4f0"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/MachineState.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0077d4f0 — `sLogDbgHelpStackFrame`

- **Адрес (Offset):** `0x0077d4f0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/MachineState.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077d4f0
static void sLogDbgHelpStackFrame(uint32_t logOptions, void (*logLineProc)(void*, const char*, ...), void* logLineProcParam, const STACKFRAME* stackFrame) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077d4f0 в IDA Pro / Ghidra
