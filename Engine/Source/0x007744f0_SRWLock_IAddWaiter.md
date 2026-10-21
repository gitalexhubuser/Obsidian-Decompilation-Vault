---
offset: "0x007744f0"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SLock.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x007744f0 — `SRWLock_IAddWaiter`

- **Адрес (Offset):** `0x007744f0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SLock.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007744f0
uint32_t SRWLock::IAddWaiter(volatile LONG* waiters, uint32_t type, uint32_t increment) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007744f0 в IDA Pro / Ghidra
