---
offset: "0x004d2aa0"
module: "WoW/Source"
file: "WoW/Source/ObjectAlloc/ObjectAlloc.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004d2aa0 — `CObjectHeap_Allocate`

- **Адрес (Offset):** `0x004d2aa0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/ObjectAlloc/ObjectAlloc.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004d2aa0
bool CObjectHeap::Allocate(uint32_t objSize, uint32_t count, const char* name) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004d2aa0 в IDA Pro / Ghidra
