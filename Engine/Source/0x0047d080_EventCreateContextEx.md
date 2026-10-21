---
offset: "0x0047d080"
module: "Engine/Source"
file: "Engine/Source/Event/Event.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0047d080 — `EventCreateContextEx`

- **Адрес (Offset):** `0x0047d080`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Event/Event.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0047d080
HEVENTCONTEXT EventCreateContextEx(int32_t interactive, EVENTHANDLERFUNC initializeHandler, EVENTHANDLERFUNC destroyHandler, uint32_t idleTime, uint32_t debugFlags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0047d080 в IDA Pro / Ghidra
