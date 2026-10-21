---
offset: "0x0077dd50"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/MachineState.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0077dd50 — `sLogX86ContextRegisters`

- **Адрес (Offset):** `0x0077dd50`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/MachineState.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077dd50
static void sLogX86ContextRegisters(void (*logLineProc)(void*, const char*, ...), void* logLineProcParam, const CONTEXT* context) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077dd50 в IDA Pro / Ghidra
