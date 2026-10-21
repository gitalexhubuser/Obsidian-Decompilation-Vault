---
offset: "0x007b1000"
module: "WoW/Source"
file: "WoW/Source/WorldClient/DetailDoodad.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007b1000 — `BuildInstanceMatrix`

- **Адрес (Offset):** `0x007b1000`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/DetailDoodad.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007b1000
static void __stdcall BuildInstanceMatrix(C33Matrix& result, C33Matrix& rotation, const C33Matrix& basis, float angle, const C3Vector& axis) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007b1000 в IDA Pro / Ghidra
