---
offset: "0x004bc290"
module: "Engine/Source"
file: "Engine/Source/Services/Profile.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004bc290 — `STRINGBLOCK_FreeString`

- **Адрес (Offset):** `0x004bc290`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Services/Profile.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004bc290
void ProfileInternal::STRINGBLOCK::FreeString(TSList<STRINGBLOCK, TSGetLink<STRINGBLOCK> >& list, char* str) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004bc290 в IDA Pro / Ghidra
