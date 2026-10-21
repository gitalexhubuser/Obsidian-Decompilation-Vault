---
offset: "0x00480d30"
module: "Engine/Source"
file: "Engine/Source/Event/EvtQueue.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00480d30 — `IEvtQueueUnregister`

- **Адрес (Offset):** `0x00480d30`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Event/EvtQueue.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00480d30
void IEvtQueueUnregister(EvtContext* context, EVENTID id, EVENTHANDLERFUNC handler, void* param, uint32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00480d30 в IDA Pro / Ghidra
