---
offset: "0x00481390"
module: "Engine/Source"
file: "Engine/Source/Event/EvtTimer.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00481390 — `IEvtTimerSet`

- **Адрес (Offset):** `0x00481390`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Event/EvtTimer.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00481390
uint32_t IEvtTimerSet(EvtContext* context, uint32_t delay, EVENTHANDLERFUNC handler, void* param, EVENTHANDLERGUIDFUNC guidHandler, uint64_t guidParam, void* guidParam2) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00481390 в IDA Pro / Ghidra
