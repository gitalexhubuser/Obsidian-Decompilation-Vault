---
offset: "0x004d2cc0"
module: "WoW/Source"
file: "WoW/Source/ObjectAlloc/ObjectAlloc.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004d2cc0 — `CObjectHeap_New`

- **Адрес (Offset):** `0x004d2cc0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/ObjectAlloc/ObjectAlloc.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004d2cc0
int32_t CObjectHeap::New(uint32_t objSize, uint32_t count, uint32_t* index, const char* name, void** ptr, bool zero) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004d2cc0 в IDA Pro / Ghidra
