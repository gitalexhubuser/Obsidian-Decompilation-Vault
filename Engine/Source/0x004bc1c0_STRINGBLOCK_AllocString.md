---
offset: "0x004bc1c0"
module: "Engine/Source"
file: "Engine/Source/Services/Profile.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004bc1c0 — `STRINGBLOCK_AllocString`

- **Адрес (Offset):** `0x004bc1c0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Services/Profile.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004bc1c0
char* ProfileInternal::STRINGBLOCK::AllocString(TSList<STRINGBLOCK, TSGetLink<STRINGBLOCK> >& list, const char* str, int32_t reuse) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004bc1c0 в IDA Pro / Ghidra
