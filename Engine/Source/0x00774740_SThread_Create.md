---
offset: "0x00774740"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SLock.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00774740 — `SThread_Create`

- **Адрес (Offset):** `0x00774740`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SLock.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00774740
int32_t SThread::Create(uint32_t (STORMAPI* threadProc)(void*), void* param, SThread& thread, char* threadName, uint32_t stackSize) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00774740 в IDA Pro / Ghidra
