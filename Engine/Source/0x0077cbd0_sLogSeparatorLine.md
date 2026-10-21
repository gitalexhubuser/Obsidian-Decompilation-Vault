---
offset: "0x0077cbd0"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/MachineState.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0077cbd0 — `sLogSeparatorLine`

- **Адрес (Offset):** `0x0077cbd0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/MachineState.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077cbd0
static void sLogSeparatorLine(void (*logLineProc)(void*, const char*, ...), void* logLineProcParam, char character, int32_t longLine) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077cbd0 в IDA Pro / Ghidra
