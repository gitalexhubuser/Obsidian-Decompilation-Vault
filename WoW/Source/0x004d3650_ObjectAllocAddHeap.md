---
offset: "0x004d3650"
module: "WoW/Source"
file: "WoW/Source/ObjectAlloc/ObjectAlloc.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004d3650 — `ObjectAllocAddHeap`

- **Адрес (Offset):** `0x004d3650`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/ObjectAlloc/ObjectAlloc.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004d3650
uint32_t ObjectAllocAddHeap(uint32_t objectSize, uint32_t objectsPerBlock, const char* name, bool freeEmptyHeaps) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004d3650 в IDA Pro / Ghidra
