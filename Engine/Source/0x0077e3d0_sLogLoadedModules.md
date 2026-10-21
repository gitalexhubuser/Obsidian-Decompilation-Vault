---
offset: "0x0077e3d0"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/MachineState.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0077e3d0 — `sLogLoadedModules`

- **Адрес (Offset):** `0x0077e3d0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/MachineState.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077e3d0
static void sLogLoadedModules(void (*logLineProc)(void*, const char*, ...), void* logLineProcParam) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077e3d0 в IDA Pro / Ghidra
