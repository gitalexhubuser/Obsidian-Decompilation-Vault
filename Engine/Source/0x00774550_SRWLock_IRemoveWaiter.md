---
offset: "0x00774550"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SLock.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00774550 — `SRWLock_IRemoveWaiter`

- **Адрес (Offset):** `0x00774550`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SLock.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00774550
int32_t SRWLock::IRemoveWaiter(volatile LONG* waiters, uint32_t expected, uint32_t type, uint32_t decrement) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00774550 в IDA Pro / Ghidra
