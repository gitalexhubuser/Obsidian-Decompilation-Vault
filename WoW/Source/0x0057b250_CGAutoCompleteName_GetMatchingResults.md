---
offset: "0x0057b250"
module: "WoW/Source"
file: "WoW/Source/Ui/CGAutoCompleteName.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0057b250 — `CGAutoCompleteName_GetMatchingResults`

- **Адрес (Offset):** `0x0057b250`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/CGAutoCompleteName.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0057b250
int32_t CGAutoCompleteName::GetMatchingResults(lua_State* L, const char* text, uint32_t include, uint32_t exclude, int32_t numReturns, int32_t cursor, bool allowFullMatch) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0057b250 в IDA Pro / Ghidra
