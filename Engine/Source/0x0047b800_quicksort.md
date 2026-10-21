---
offset: "0x0047b800"
module: "Engine/Source"
file: "Engine/Source/Base/Sort.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0047b800 — `quicksort`

- **Адрес (Offset):** `0x0047b800`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Base/Sort.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0047b800
void quicksort(void* base, uint32_t num, uint32_t width, int32_t (*comp)(const void*, const void*, void*), void* context) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0047b800 в IDA Pro / Ghidra
