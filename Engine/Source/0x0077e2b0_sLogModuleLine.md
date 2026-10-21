---
offset: "0x0077e2b0"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/MachineState.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0077e2b0 — `sLogModuleLine`

- **Адрес (Offset):** `0x0077e2b0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/MachineState.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077e2b0
static void sLogModuleLine(void (*logLineProc)(void*, const char*, ...), void* logLineProcParam, void* base, const char* name, uint32_t size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077e2b0 в IDA Pro / Ghidra
