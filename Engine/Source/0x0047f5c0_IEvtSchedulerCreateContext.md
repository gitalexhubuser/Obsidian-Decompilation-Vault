---
offset: "0x0047f5c0"
module: "Engine/Source"
file: "Engine/Source/Event/EvtSched.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0047f5c0 — `IEvtSchedulerCreateContext`

- **Адрес (Offset):** `0x0047f5c0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Event/EvtSched.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0047f5c0
HEVENTCONTEXT IEvtSchedulerCreateContext(int32_t interactive, EVENTHANDLERFUNC initializeHandler, EVENTHANDLERFUNC destroyHandler, uint32_t idleTime, uint32_t debugFlags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0047f5c0 в IDA Pro / Ghidra
