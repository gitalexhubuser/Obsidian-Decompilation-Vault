---
offset: "0x00770260"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SThread.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00770260 — `SCreateThread`

- **Адрес (Offset):** `0x00770260`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SThread.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00770260
HANDLE STORMAPI SCreateThread(uint32_t (STORMAPI* lpStartAddress)(void*), void* lpParameter, uint32_t* lpThreadId, void* linuxData, char* threadName, uint32_t stackSize) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00770260 в IDA Pro / Ghidra
