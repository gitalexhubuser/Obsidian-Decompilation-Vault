---
offset: "0x0077cca0"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/MachineState.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0077cca0 — `sLogMemoryHexDump`

- **Адрес (Offset):** `0x0077cca0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/MachineState.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077cca0
static void sLogMemoryHexDump(void (*logLineProc)(void*, const char*, ...), void* logLineProcParam, uint8_t* address, uint32_t numBytes, int32_t alignedLines) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077cca0 в IDA Pro / Ghidra
