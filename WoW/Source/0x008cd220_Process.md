---
offset: "0x008cd220"
module: "WoW/Source"
file: "WoW/Source/WowServices/Grunt.h"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008cd220 — `Process`

- **Адрес (Offset):** `0x008cd220`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/Grunt.h`

## Сигнатура C++
```cpp
// OFFSET: 0x008cd220
template <class T> bool Grunt::Command<T>::Process(CDataStore& msg, Grunt::Command<T>* commands, uint32_t commandCount, T& object, uint32_t& pos) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008cd220 в IDA Pro / Ghidra
