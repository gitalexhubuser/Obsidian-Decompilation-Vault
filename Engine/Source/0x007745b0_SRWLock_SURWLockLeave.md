---
offset: "0x007745b0"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SLock.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x007745b0 — `SRWLock_SURWLockLeave`

- **Адрес (Offset):** `0x007745b0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SLock.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007745b0
void SRWLock::SURWLockLeave(volatile SURWLOCK* surwlock, int32_t fromwriting) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007745b0 в IDA Pro / Ghidra
