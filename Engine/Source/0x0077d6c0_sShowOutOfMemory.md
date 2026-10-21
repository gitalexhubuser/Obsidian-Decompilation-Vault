---
offset: "0x0077d6c0"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/MachineState.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0077d6c0 — `sShowOutOfMemory`

- **Адрес (Offset):** `0x0077d6c0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/MachineState.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077d6c0
static void sShowOutOfMemory(void (*logLineProc)(void*, const char*, ...), void* logLineProcParam) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077d6c0 в IDA Pro / Ghidra
