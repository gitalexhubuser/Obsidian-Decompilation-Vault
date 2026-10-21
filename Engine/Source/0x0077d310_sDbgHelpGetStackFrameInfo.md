---
offset: "0x0077d310"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/MachineState.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0077d310 — `sDbgHelpGetStackFrameInfo`

- **Адрес (Offset):** `0x0077d310`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/MachineState.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0077d310
static int32_t sDbgHelpGetStackFrameInfo(DWORD_PTR address, char* moduleName, char* symbolName, uint32_t* symbolDisplacement, char* fileName, uint32_t* lineNumber) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0077d310 в IDA Pro / Ghidra
