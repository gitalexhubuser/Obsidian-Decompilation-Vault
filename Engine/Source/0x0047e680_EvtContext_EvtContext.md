---
offset: "0x0047e680"
module: "Engine/Source"
file: "Engine/Source/Event/EvtContext.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0047e680 — `EvtContext_EvtContext`

- **Адрес (Offset):** `0x0047e680`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Event/EvtContext.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0047e680
EvtContext::EvtContext(uint32_t flags, uint32_t idleTime, uint32_t schedWeight, void* callContext, int32_t startWatchdog) : m_timerQueue(offsetof(EvtTimer, m_targetTime)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0047e680 в IDA Pro / Ghidra
