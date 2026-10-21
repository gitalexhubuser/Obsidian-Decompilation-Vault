---
offset: "0x004d3250"
module: "WoW/Source"
file: "WoW/Source/ObjectAlloc/ObjectAlloc.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004d3250 — `CObjectHeapList_New`

- **Адрес (Offset):** `0x004d3250`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/ObjectAlloc/ObjectAlloc.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004d3250
int32_t CObjectHeapList::New(uint32_t* index, void** ptr, bool zero) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004d3250 в IDA Pro / Ghidra
