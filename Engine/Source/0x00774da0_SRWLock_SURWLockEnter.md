---
offset: "0x00774da0"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SLock.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00774da0 — `SRWLock_SURWLockEnter`

- **Адрес (Offset):** `0x00774da0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SLock.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00774da0
void SRWLock::SURWLockEnter(volatile SURWLOCK* surwlock, int32_t forwriting) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00774da0 в IDA Pro / Ghidra
