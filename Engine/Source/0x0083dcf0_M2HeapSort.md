---
offset: "0x0083dcf0"
module: "Engine/Source"
file: "Engine/Source/Model2/M2Shared.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0083dcf0 — `M2HeapSort`

- **Адрес (Offset):** `0x0083dcf0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Model2/M2Shared.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0083dcf0
void M2HeapSort(int32_t (*compare)(uint32_t, uint32_t, const void*), uint32_t* array, uint32_t count, const void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0083dcf0 в IDA Pro / Ghidra
