---
offset: "0x004804f0"
module: "Engine/Source"
file: "Engine/Source/Event/EvtQueue.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004804f0 — `IEvtQueueRegister`

- **Адрес (Offset):** `0x004804f0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Event/EvtQueue.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004804f0
void IEvtQueueRegister(EvtContext* context, EVENTID id, EVENTHANDLERFUNC handler, void* param, float priority) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004804f0 в IDA Pro / Ghidra
