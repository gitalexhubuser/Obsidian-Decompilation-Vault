---
offset: "0x0077d860"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/MachineState.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0077d860 — `sLogDbgHelpStackTrace`

- **Адрес (Offset):** `0x0077d860`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/MachineState.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077d860
static void sLogDbgHelpStackTrace(uint32_t logOptions, void (*logLineProc)(void*, const char*, ...), void* logLineProcParam, DWORD_PTR registerEip, DWORD_PTR registerEbp, DWORD_PTR registerEsp, uint32_t stackFramesToSkip) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077d860 в IDA Pro / Ghidra
