---
offset: "0x007700a0"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SThread.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x007700a0 — `SCreateThread`

- **Адрес (Offset):** `0x007700a0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SThread.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007700a0
HANDLE SCreateThread(uint32_t dwStackSize, uint32_t (STORMAPI* lpStartAddress)(void*), void* lpParameter, uint32_t dwCreationFlags, uint32_t* lpThreadId, char* threadName) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007700a0 в IDA Pro / Ghidra
