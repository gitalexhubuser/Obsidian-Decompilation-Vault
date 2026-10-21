---
offset: "0x007746b0"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SLock.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x007746b0 — `SSyncObject_WaitMultiplePtr`

- **Адрес (Offset):** `0x007746b0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SLock.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007746b0
uint32_t STORMAPI SSyncObject::WaitMultiplePtr(uint32_t count, SSyncObject** objects, int32_t waitAll, uint32_t timeout) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007746b0 в IDA Pro / Ghidra
