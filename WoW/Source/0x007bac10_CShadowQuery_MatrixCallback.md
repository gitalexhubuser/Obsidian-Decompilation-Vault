---
offset: "0x007bac10"
module: "WoW/Source"
file: "WoW/Source/WorldClient/ShadowQuery.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007bac10 — `CShadowQuery_MatrixCallback`

- **Адрес (Offset):** `0x007bac10`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/ShadowQuery.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007bac10
void CShadowQuery::MatrixCallback(C3Vector& center, float radius, C44Matrix& matrix, C3Vector& direction, int32_t band) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007bac10 в IDA Pro / Ghidra
