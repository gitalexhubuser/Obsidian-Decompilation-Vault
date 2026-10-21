---
offset: "0x008c65f0"
module: "WoW/Source"
file: "WoW/Source/Battlenet/Battlenet.h"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008c65f0 — `Allocator_Delete`

- **Адрес (Offset):** `0x008c65f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/Battlenet.h`

## Сигнатура C++
```cpp
// OFFSET: 0x008c65f0
template <class T> void Battlenet::Allocator::Delete(T*& object) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008c65f0 в IDA Pro / Ghidra
