---
offset: "0x0077db10"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/MachineState.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0077db10 — `sLogX86ManualStackTrace`

- **Адрес (Offset):** `0x0077db10`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/MachineState.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077db10
static void sLogX86ManualStackTrace(void (*logLineProc)(void*, const char*, ...), void* logLineProcParam, DWORD_PTR registerEip, DWORD_PTR registerEbp, uint32_t stackFramesToSkip) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077db10 в IDA Pro / Ghidra
