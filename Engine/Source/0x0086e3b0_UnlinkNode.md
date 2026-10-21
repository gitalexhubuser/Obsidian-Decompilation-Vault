---
offset: "0x0086e3b0"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsTcp.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0086e3b0 — `UnlinkNode`

- **Адрес (Offset):** `0x0086e3b0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsTcp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0086e3b0
template <class T, int LINKOFFSET, int SLOTS> void OsNet::TSSlottedListEx<T, LINKOFFSET, SLOTS>::UnlinkNode(T* ptr, uint8_t slot) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0086e3b0 в IDA Pro / Ghidra
